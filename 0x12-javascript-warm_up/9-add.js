#!/usr/bin/node
const arg = process.argv.splice(2, 2);
if ((!isNaN(Number(arg[0]))) && (!isNaN(Number(arg[1])))) {
  console.log(add(Number(arg[0]), Number(arg[1])));
} else {
  console.log('NaN');
}

function add (a, b) {
  return (a + b);
}
