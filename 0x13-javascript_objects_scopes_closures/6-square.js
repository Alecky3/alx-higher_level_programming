#!/usr/bin/node
const MySquare = require('./5-square.js');
class Square extends MySquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      console.log(c === undefined ? 'X'.repeat(this.width) : c.repeat(this.width));
    }
  }
}
module.exports = Square;
