#!/usr/bin/node
const arg = process.argv.splice(2, 1);

if (!isNaN(Number(arg[0]))) {
  let i = parseInt(arg[0]);
  let j = i;
  const list = [];
  while (i > 0) {
    list.push('X');
    i--;
  }
  while (j > 0) {
    console.log(list.join(''));
    j--;
  }
} else {
  console.log('Missing size');
}
