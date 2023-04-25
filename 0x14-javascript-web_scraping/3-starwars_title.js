#!/usr/bin/node
const req = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
req(url + movieId, function (err, res, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(data).title);
  }
});
