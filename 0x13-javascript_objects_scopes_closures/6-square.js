#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let string = '';
      for (let i = 0; i < this.width; i++) {
        string = string + c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(string);
      }
    }
  }
};
