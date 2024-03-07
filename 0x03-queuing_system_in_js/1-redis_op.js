#!/usr/bin/npm dev

import { createClient, print } from 'redis';
const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (school_name, value) => {
  client.SET(school_name, value, print);
};

const displaySchoolValue = (school_name) => {
  client.GET(school_name, (_err, res) => {
    console.log(res);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
