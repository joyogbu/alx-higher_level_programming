#!/usr/bin/node
const arg = process.argv;
const url = arg[2];
let i = 0;
let count = 0;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const myData = data.results;
  for (i = 0; i < data.results.length; i++) {
    for (let j = 0; j < myData[i].characters.length; j++) {
      if ((myData[i].characters[j]).endsWith('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
