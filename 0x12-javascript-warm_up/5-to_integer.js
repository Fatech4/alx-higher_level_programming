#!/usr/bin/node
const arg = process.argv.splice(2, 1);

if (!isNaN(Number(arg[0]))) {
  console.log(`My number: ${parseInt(arg[0])}`);
} else {
  console.log('Not a number');
}
