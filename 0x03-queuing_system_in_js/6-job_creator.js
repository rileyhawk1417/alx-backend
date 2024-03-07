#!/usr/bin/npm dev

import { createQueue } from 'kue';

const que = createQueue({ name: 'push_notification_code' });
const job = que.create('push_notification_code', {
  phoneNumber: '071257390823',
  message: 'This is the code to verify your account',
});

job
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });
job.save();
