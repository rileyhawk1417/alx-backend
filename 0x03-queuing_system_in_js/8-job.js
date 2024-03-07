#!/usr/bin/npm

function createPushNotificationsJobs(jobs, que) {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const job of jobs) {
    const job_data = que.create('push_notification_code_3', job);
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
}

export default createPushNotificationsJobs;
