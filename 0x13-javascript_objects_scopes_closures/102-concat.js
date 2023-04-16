#!/usr/bin/node
const arg = process.argv.splice(2);
const fs = require('fs');
const file1 = arg[0];
const file2 = arg[1];
const destFile = arg[2];
function concatFiles (file1, file2, destFile) {
  const content1 = fs.readFile(file1);
  const content2 = fs.readFile(file2);
  fs.writeFile(destFile, content1 + content2);
}
concatFiles(file1, file2, destFile);
