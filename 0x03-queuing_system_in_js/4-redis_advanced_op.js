#!/usr/bin/npm dev

import { createClient, print } from 'redis';
const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server', err.toString());
});

const hashUpdater = (hashName, fieldName, fieldValue) => {
  client.HSET(hashName, fieldName, fieldValue, print);
};

const hashPrinter = (hashName) => {
  client.HGETALL(hashName, (_err, res) => console.log(res));
};

function main() {
  const hash = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  for (const [field, value] of Object.entries(hash)) {
    hashUpdater('HolbertonSchools', field, value);
  }
  hashPrinter('HolbertonSchools');
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
