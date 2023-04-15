#!/usr/bin/node
const ParentSquare = require('./5-square.js');

class Square extends ParentSquare {
  constructor(size) {
    super(size);
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
