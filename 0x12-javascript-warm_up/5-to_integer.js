#!/usr/bin/node
const arg = process.argv;
console.log(typeof Number(arg[2]));
const arg1 = Number(arg[2]);
if (Number.isInteger(arg1)){
  console.log('My number is ' + arg1);
} else {
  console.log('Not a number');
}
