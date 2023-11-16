#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let character = 'X';
    character = character.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(character);
    }
  }
}
module.exports = Rectangle;
