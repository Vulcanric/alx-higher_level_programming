#!/usr/bin/node
/* Computes factorial */

// Function that computes the factorial of an integer
function factorial (n) {
  if (!n) {
    return 1;
  }
  return n * factorial(n - 1);
}

const n = parseInt(process.argv[2]);
console.log(factorial(n));
