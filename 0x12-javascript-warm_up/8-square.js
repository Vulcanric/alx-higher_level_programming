#!/usr/bin/node
/* Even more loops: WHILE loop => Program that logs to stdout a square of size n */

const size = parseInt(process.argv[2]); // first argument passed
let character = 'X';
let i = 0;

try {
  character = character.repeat(size);
} catch (err) {
  process.exit(0);
}

if (!size) {
  console.log('Missing size');
} else {
  while (i < size) {
    console.log(character);
    i++;
  }
}
