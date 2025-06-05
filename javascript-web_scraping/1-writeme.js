#!/usr/bin/node
const request = require('fs');

request.writeFile(process.argv[2], process.argv[3], (error, data) => {
  if (error) {
    console.log(error);
  }
});
