#!/usr/bin/node
const idMovie = process.argv[2]
const req = require('request');
const starApi = 'https://swapi-api.hbtn.io/api/films/'.concat(idMovie);

req(starApi, function (_error, _respond, obj){
  obj = JSON.parse(obj);
  console.log(obj.title);
});
