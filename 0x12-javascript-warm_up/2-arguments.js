#!/usr/bin/node

// Access commandline arguments passed to the process.
// Javascript cmdline arguments implicitly start with 'node',
// then the name of the 'program', therefore when no args
// are passed, the length would be 2

/* console.log(process.argv.join(" ")); */
/* console.log(process.argv.length); */
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
