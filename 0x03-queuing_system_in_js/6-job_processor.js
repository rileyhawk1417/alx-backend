#!/usr/bin/npm dev

import { createQueue } from 'kue';

const que = createQueue({ name: 'push_notification_code' });

const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber},`,
    'with message:',
    message,
  );
};

que.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
