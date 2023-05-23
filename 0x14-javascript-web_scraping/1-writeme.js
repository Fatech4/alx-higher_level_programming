#!/usr/bin/node

const arg = process.argv[2];
const data = process.argv[3];
const res = require('fs');
res.writeFile(arg, data, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
