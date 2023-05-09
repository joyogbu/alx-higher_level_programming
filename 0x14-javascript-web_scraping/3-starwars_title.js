#!/usr/bin/node
const arg = process.argv;
const number = arg[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + number;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
