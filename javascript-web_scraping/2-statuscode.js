#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (error, res) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
