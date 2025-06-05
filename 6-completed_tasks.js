#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (error, res, body) => {
  if (error) {
    console.log(error);
  }
  const responses = {};
  JSON.parse(body).filter(item => item.completed).forEach(item => {
    if (responses[item.userId] === undefined) {
      responses[item.userId] = 1;
    } else {
      responses[item.userId] = responses[item.userId] + 1;
    }
  });
  console.log(responses);
});
