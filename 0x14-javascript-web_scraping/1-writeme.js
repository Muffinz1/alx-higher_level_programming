#!/usr/bin/node

const f = require('fs');
const fileName = process.argv[2];
const fileInput = process.argv[3];
const fileContent = 'utf8';
f.writeFile(fileName, fileInput, fileContent, function (error) {
  if (error) {
    console.log(error);
  }
});
