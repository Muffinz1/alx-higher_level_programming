#!/usr/bin/node

const f = require('fs');
const fileName = process.argv[2];
const fileContent = 'utf8';
f.readFile(fileName, fileContent, function (error, data) {
  if (error) {
    console.log(error);
  } else {
    process.stdout.write(data);
  }
});
