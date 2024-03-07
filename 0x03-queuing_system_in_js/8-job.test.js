#!/usr/bin/npm test
import sinon from 'sinon';
import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job';

const demo_data = [
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  const spy_console = sinon.spy(console);
  const que = createQueue({ name: 'push_notification_code_test' });

  before(() => {
    que.testMode.enter(true);
  });

  after(() => {
    que.testMode.clear();
    que.testMode.exit();
  });

  afterEach(() => {
    spy_console.log.resetHistory();
  });

  it('display error if jobs not an array', () => {
    expect(
      createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, que),
    ).to.throw('Jobs is not an array');
  });

  it('add job(s) to queue if types match', (done) => {
    expect(que.testMode.jobs.length).to.equal(0);
    createPushNotificationsJobs(demo_data, que);
    expect(que.testMode.jobs.length).to.equal(demo_data.length);
    expect(que.testMode.jobs[0].data).to.deep.equal(demo_data[0]);
    expect(que.testMode.jobs[0].type).to.equal('push_notification_code_3');
    que.process('push_notification_code_3', () => {
      expect(
        spy_console.log.calledWith(
          'Notification job created:',
          que.testMode.jobs[0].id,
        ),
      ).to.be.true;
      done();
    });
  });
  it('test progress event handler for job', (done) => {
    que.testMode.jobs[0].addListener('progress', () => {
      expect(
        spy_console.log.calledWith(
          'Notification job',
          que.testMode.jobs[0].id,
          '25% complete',
        ),
      ).to.be.true;
      done();
    });
    que.testMode.jobs[0].emit('progress', 25);
  });

  it('test failed event handler for job', (done) => {
    que.testMode.jobs[0].addListener('failed', () => {
      expect(
        spy_console.log.calledWith(
          'Notification job',
          que.testMode.jobs[0].id,
          'failed:',
          'Failed to send',
        ),
      ).to.be.true;
      done();
    });
    que.testMode.jobs[0].emit('failed', new Error('Failed to send'));
  });

  it('test complete event handler for job', (done) => {
    que.testMode.jobs[0].addListener('complete', () => {
      expect(
        spy_console.log.calledWith(
          'Notification job',
          que.testMode.jobs[0].id,
          'completed',
        ),
      ).to.be.true;
      done();
    });
    que.testMode.jobs[0].emit('complete');
  });
});
