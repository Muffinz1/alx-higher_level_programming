#!/usr/bin/node

const arg = process.argv[2];
let loop = Math.floor(Number(arg));
if (Number.isInteger(loop)) {
  while (loop > 0) {
    console.log('C is fun');
    loop = loop - 1;
  }
} else {
  console.log('Missing number of occurrences');
}
