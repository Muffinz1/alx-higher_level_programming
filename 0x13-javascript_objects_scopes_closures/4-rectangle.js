#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    let h = this.height;
    while (h > 0) {
      console.log('X'.repeat(this.width));
      h = h - 1;
    }
  }

  double () {
    let h = this.height * 2;
    const w = this.width * 2;
    while (h > 0) {
      console.log('X'.repeat(w));
      h = h - 1;
    }
  }

  rotate () {
    let h = this.width;
    const w = this.height;
    while (h > 0) {
      console.log('X'.repeat(w));
      h = h - 1;
    }
  }
}
module.exports = Rectangle;
