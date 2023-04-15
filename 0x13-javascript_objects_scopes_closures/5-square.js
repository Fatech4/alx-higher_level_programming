#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super();
    this.size = size;
  }

  print () {
    super.print();
  }

  double () {
    super.double();
  }

  rotate () {
    super.rotate();
  }
};
