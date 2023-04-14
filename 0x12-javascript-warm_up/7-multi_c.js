#!/usr/bin/node
const arg = process.argv.splice(2, 1);
if (!isNaN(Number(arg[0]))) {
  let i = parseInt(arg[0]);
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
