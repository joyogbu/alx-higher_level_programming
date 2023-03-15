#!/usr/bin/node
const arr = require('./100-data.js');
const map1 = arr.list.map((x, index) => x * index);
console.log(arr.list);
console.log(map1);
