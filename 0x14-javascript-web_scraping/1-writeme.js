#!/usr/bin/node
const arg = process.argv;
const path = arg[2];
const data = arg[3];
const fs = require('fs');
fs.writeFile(path, data, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
