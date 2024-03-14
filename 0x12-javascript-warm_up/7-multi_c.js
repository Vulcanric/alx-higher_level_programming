#!/usr/bin/node
const { argv } = require('node:process');

numberOfOcurrence = Number(argv[2]);
if (numberOfOcurrence) {
  for (let i = 0; i < numberOfOcurrence; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
