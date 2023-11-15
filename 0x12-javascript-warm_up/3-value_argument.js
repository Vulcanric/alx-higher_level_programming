#!/usr/bin/node

// ARGV[0] => process.execPath = /usr/bin/node
// ARGV[1] => path to js file being executed
// ARGV[1+n] = Any other additional argument passed

/* Import the process object */
const { argv } = require('node:process');

/* When no arguments are passed to the program */
if (process.argv.length === 2) { console.log('No argument'); } else {
  argv.forEach((val, index) => {
    if (index > 1) { console.log(`${val}`); }
  });
}
