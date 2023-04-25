#!/usr/bin/node
const req = require('request');

const url = process.argv[2];
req(url, function (err, res, data) {
  if (err == null) {
    const films = JSON.parse(data).results;
    const result = films.reduce((count, item) => {
      return item.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0);
    console.log(result);
  }
});
