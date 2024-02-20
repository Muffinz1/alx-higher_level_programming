#!/usr/bin/node
const sauce = require('./5-square');
class Square extends sauce {
  charPrint (c) {
    let count = this.height;
    if (c === undefined) {
      this.print();
    } else {
      while (count > 0) {
        console.log(c.repeat(this.height));
        count = count - 1;
      }
    }
  }
}
module.exports = Square;
