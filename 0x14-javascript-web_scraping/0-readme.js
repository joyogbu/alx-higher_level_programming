#!/usr/bin/node
const arg = process.argv;
const url = arg[2];
const fs = require("fs");
fs.readFile(url, "utf-8", function(err, buf) {
         if(err) {
              console.log(err);
         }
         console.log(buf);
});
