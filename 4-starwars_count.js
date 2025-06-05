#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request.get(id, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).results.filter(element => element.characters.find(character => character.includes('18'))).length);
  }
});
