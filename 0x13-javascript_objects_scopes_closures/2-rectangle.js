#!/usr/bin/node
let myObj;
class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  //}
    if (w === 0 || h === 0 || w < 0 || h < 0) {
      myObj = new Rectangle();
      return (myObj);
    }
  }
};
module.exports = Rectangle;
