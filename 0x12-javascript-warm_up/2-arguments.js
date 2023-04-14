#!/usr/bin/node

const arg = process.argv.splice(2);
if (arg.length === 0) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
