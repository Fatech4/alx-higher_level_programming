#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const wide = [];
    for (let i = 1; i <= this.width; i++) {
      wide.push('X');
    }
    for (let j = 1; j <= this.height; j++) {
      console.log(wide.join(''));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

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
