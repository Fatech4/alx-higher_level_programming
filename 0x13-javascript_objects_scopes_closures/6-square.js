#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
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

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      const wide = [];
      for (let i = 1; i <= this.width; i++) {
        wide.push('C');
      }
      for (let j = 1; j <= this.height; j++) {
        console.log(wide.join(''));
      }
    }
  }
};
