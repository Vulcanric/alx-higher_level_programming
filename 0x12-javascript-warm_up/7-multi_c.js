#!/usr/bin/node
/* More loops */

const numberOfOccurrence = parseInt(process.argv[2]);

if (!numberOfOccurrence) {
  console.log("Missing number of occurrences");
} else {
  for (let i = 0; i < numberOfOccurrence; i++) {
    console.log("C is fun");
  }
}
