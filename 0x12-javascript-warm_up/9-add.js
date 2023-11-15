#!/usr/bin/node
/* Prints to stdout, the sum of 2 integers */

// Function that returns the addition of 2 integers
function add (a, b) {
  return a + b;
}
// Get the 2 numbers
const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);
// Print the result to stdout
console.log(add(first, second));
