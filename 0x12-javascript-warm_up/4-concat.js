#!/usr/bin/node
/* Program that logs to stdout the 1st argument `is` 2nd argument */

// ARGV[0] => process.execPath = /usr/bin/node
// ARGV[1] => path to js file being executed
// ARGV[1+n] = Any other additional argument passed

const args = process.argv;
console.log(`${args[2]} is ${args[3]}`);
