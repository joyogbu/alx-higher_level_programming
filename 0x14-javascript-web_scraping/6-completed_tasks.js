#!/usr/bin/node
const arg = process.argv;
const url = arg[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const myData = JSON.parse(body);
  const myDict = {};
  for (let i = 0; i < myData.length; i++) {
    if (myData[i].completed === true) {
      if (myDict[myData[i].userId]) {
        myDict[myData[i].userId] += 1;
      } else {
        myDict[myData[i].userId] = 1;
      }
    }
  }
  console.log(myDict);
});
