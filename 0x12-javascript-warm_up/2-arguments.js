#!/usr/bin/node

let args = process.argv.length;
args = args - 1;

if (args === 1) {
  console.log('No argument');
} else if (args === 2) {
  console.log('Argument found');
} else if (args > 2) {
  console.log('Arguments found');
}
