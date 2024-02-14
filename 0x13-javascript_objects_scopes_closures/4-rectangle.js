#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    let count = this.height;
    while (count > 0) {
      console.log('X'.repeat(this.width));
      count = count - 1;
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const Oh = this.height;
    this.height = this.width;
    this.width = Oh;
  }
}

module.exports = Rectangle;
