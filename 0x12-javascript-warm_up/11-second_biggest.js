#!/usr/bin/node
/* Program that finds the second biggest nummber in an array */

const args = process.argv.map((n) => parseInt(n)); // Convert each string to int
const numbers = args.filter((v) => !(!v)); // Removes all the NaN's

if (args.length === 2 || numbers.length === 1) { // One or no argument passed
  console.log(0);
} else {
  numbers.sort();
  const secondLargest = numbers.slice(-2, -1)[0];
  console.log(secondLargest);
}
