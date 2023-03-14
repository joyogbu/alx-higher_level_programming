#!/usr/bin/node
const arg = process.argv;
const arg1 = Number(arg[2]);
const arg2 = Number(arg[3]);
function add (a, b) {
  return a + b;
}
console.log(add(arg1, arg2));
