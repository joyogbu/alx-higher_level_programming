#!/usr/bin/node
const arg = process.argv;
const url = arg[2];
const path = arg[3];
const request = require('request');
const fs = require('fs');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(path, body, function (err) {
    if (err) {
      console.log(err);
    }
  });
});
