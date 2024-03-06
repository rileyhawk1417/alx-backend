#!/usr/bin/npm dev

import { createQueue } from 'kue';

const que = createQueue({ name: 'push_notification_code_2' });

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

for (const job of jobs) {
  const job_data = que.create('push_notification_code_2', job);
  job_data
    .on('enqueue', () => {
      console.log('Notification job created:', job_data.id);
    })
    .on('complete', () => {
      console.log('Notification job', job_data.id, 'completed');
    })
    .on('failed', (err) => {
      console.log(
        'Notification job',
        job_data.id,
        'failed:',
        err.message || err.toString(),
      );
    })
    .on('progress', (progress, _data) => {
      console.log('Notification job', job_data.id, `${progress}% complete`);
    });
  job_data.save();
}
