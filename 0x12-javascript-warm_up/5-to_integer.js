#!/usr/bin/node

const arg = process.argv[2];
const test = parseFloat(arg);

if (Number.isInteger(test)) {
  console.log('My number:',arg);
} else {
  console.log('Not a number');
}
