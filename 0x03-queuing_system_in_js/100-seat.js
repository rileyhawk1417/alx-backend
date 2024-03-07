#!/usr/bin/npm dev

import express from 'express';
import { promisify } from 'util';
import { createQueue } from 'kue';
import { createClient } from 'redis';
import { X509Certificate } from 'crypto';

const app = express();
const PORT = 1245;
const client = createClient({ name: 'reserve_seat' });
const que = createQueue();
const init_seat_count = 50;
let reservationEnabled = false;

function reserveSeat(number) {
  return promisify(client.SET).bind(client)('available_seats', number);
}

function getCurrentAvailableSeats() {
  return promisify(client.GET).bind(client)('available_seats');
}

function resetSeatCount(number) {
  return promisify(client.SET).bind(client)(
    'available_seats',
    Number.parseInt(number),
  );
}

app.get('/available_seats', (_, res) => {
  getCurrentAvailableSeats().then((numberOfSeats) => {
    res.json({ numberOfSeats });
  });
});

app.get('/reserve_seat', (_req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }
  try {
    const job = que.create('reserve_seat');
    job.on('failed', (err) => {
      console.log(
        'Seat reservation job',
        job.id,
        'failed:',
        err.message || err.toString(),
      );
    });
    job.on('complete', () => {
      console.log('Seat reservation job', job.id, 'completed');
    });
    job.save();
    res.json({ status: 'Reservation in process' });
  } catch {
    res.json({ status: 'Reservation failed' });
  }
});

app.get('/process', (_req, res) => {
  res.json({ status: 'Queue processing' });
  que.process('reserve_seat', (_job, done) => {
    getCurrentAvailableSeats()
      .then((result) => Number.parseInt(result || 0))
      .then((available_seats) => {
        reservationEnabled = available_seats <= 1 ? false : reservationEnabled;
        if (available_seats >= 1) {
          reserveSeat(available_seats - 1).then(() => done());
        } else {
          done(new Error('Not enough seats avaiable'));
        }
      });
  });
});

app.listen(PORT, () => {
  resetSeatCount(process.env.INITIAL_SEATS_COUNT || init_seat_count).then(
    () => {
      reservationEnabled = true;
      console.log(`Listening on port ${PORT}`);
    },
  );
});
export default app;
