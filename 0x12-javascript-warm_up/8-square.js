#!/usr/bin/node

const arg = process.argv[2];
const size = Math.floor(Number(arg));
let count = size;

if (Number.isInteger(size)) {
  while (count > 0) {
    console.log('X'.repeat(size));
    count = count - 1;
  }
} else {
  console.log('Missing size');
}
