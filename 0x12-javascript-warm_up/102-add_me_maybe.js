#!/usr/bin/node
let count = 0;
exports.addMeMaybe = function (number, theFunction) {
  count++;
  theFunction(number + count);
};
