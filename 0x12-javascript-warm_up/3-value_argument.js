#!/usr/bin/node
/* Program that logs to stdout the first argument that was passed to it */

// ARGV[0] => process.execPath = /usr/bin/node
// ARGV[1] => path to js file being executed
// ARGV[1+n] = Any other additional argument passed

let args = process.argv;
args = args.slice(2, 3); // Cutting out argv[0] and argv[1]

if (args.toString() === '') {
  console.log('No argument');
} else {
  console.log(`${args[0]}`);
}
