#!/usr/bin/npm dev

import { createQueue } from 'kue';

const que = createQueue({ name: 'push_notification_code' });
const job = que.create('push_notification_code', {
  phoneNumber: '0712573820128',
  message: 'Account registered',
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
