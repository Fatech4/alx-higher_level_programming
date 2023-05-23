#!/usr/bin/node

const arg = process.argv[2];
const res = require('fs');
res.readFile(arg, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
