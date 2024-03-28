#!/usr/bin/node
const request = require('request');
const starInput = process.argv[2];
let count = 0;

request(starInput, function (_error, _respond, obj) {
  obj = JSON.parse(obj).results;

  for (let x = 0; x < obj.length; ++x) {
    const chars = obj[x].chars;

    for (let y = 0; y < chars.length; ++y) {
      const chara = chars[y];
      const charaId = chara.split('/')[5];
      if (charaId === '18') {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
