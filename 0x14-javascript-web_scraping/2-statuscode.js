#!/usr/bin/node
const arg = process.argv;
const url = arg[2];
const request = require('request');
request.get(url, function (req, res) {
  console.log('code: ' + res.statusCode);
});
