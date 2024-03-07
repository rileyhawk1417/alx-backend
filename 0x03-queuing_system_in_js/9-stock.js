#!/usr/bin/npm dev

import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailablityQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailablityQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailablityQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailablityQuantity: 5,
  },
];

function getItemById(id) {
  const item = listProducts.find((product) => product.itemId === id);
  return item;
}

// Redis Functions
function reserveStockById(itemId, stock) {
  return promisify(client.SET).bind(client)(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  return promisify(client.GET).bind(client)(`item.${itemId}`);
}

const app = express();
const client = createClient();
const PORT = 1245;

app.get('/list_products', (_, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId(\\d+)', (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }
  getCurrentReservedStockById(itemId)
    .then((result) => Number.parseInt(result) || 0)
    .then((reserved) => {
      item.currentQuantity = item.initialAvailablityQuantity - reserved;
      res.json(item);
    });
});

app.get('/reserve_product/:itemId(\\d+)', (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }
  getCurrentReservedStockById(itemId)
    .then((result) => Number.parseInt(result) || 0)
    .then((reserved) => {
      if (reserved >= item.initialAvailablityQuantity) {
        res.json({ status: 'Not enough stock avaiable', itemId });
        return;
      }
      reserveStockById(itemId, reserved + 1).then(() => {
        res.json({ status: 'Reservation confirmed', itemId });
      });
    });
});

app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});
export default app;
