#!/usr/bin/node
const arg = process.argv;
const arg1 = Number(arg[2]);
if (Number.isInteger(arg1)) {
  console.log('My number:' + arg1);
} else {
  console.log('Not a number');
}
