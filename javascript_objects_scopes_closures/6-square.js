#!/usr/bin/node
const BigSquare = require('./5-square');

class Square extends BigSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      console.log((c || 'X').repeat(this.width));
    }
  }
}
module.exports = Square;
