#!/usr/bin/node
const arg = process.argv.splice(2, 1);

if (arg.toString() === '') {
  console.log('No argument');
} else {
  console.log(arg[0]);
}
