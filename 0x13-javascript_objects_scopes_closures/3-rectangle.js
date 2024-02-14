#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    while (this.height > 0) {
      console.log('X'.repeat(this.width));
      this.height = this.height - 1;
    }
  }
}
module.exports = Rectangle;
