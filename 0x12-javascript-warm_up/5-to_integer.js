#!/usr/bin/node
/* Program that logs to stdout "My number: int-of argv[2]" */
/* if argv[2] is a number OR "Not a Number" if it is not */

// ARGV[0] => process.execPath = /usr/bin/node
// ARGV[1] => path to js file being executed
// ARGV[1+n] = Any other additional argument passed

const args = process.argv;
const convert = parseInt(args[2]); // Convert 1st argument to integer

if (!convert) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convert}`);
}
