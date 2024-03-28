#!/usr/bin/node

const request = require('request');
const starApi = process.argv[2];
let count = 0;

request(starApi, function (_err, _res, obj) {
  obj = JSON.parse(obj).results;

  for (let x = 0; x < obj.length; ++i) {
    const chars = body[x].chars;

    for (let y = 0; y < chars.length; ++y) {
      const chr = chars[y];
      const charId = chr.split('/')[5];

      if (charId === '18') {
        count += 1;
      }
    }
  }

  console.log(count);
});
