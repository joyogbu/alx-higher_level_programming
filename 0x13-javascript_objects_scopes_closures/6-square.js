#!/usr/bin/node
let i;
const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
