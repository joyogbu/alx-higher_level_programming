#!/usr/bin/node
const arg = process.argv;
let i;
const arg1 = Number(arg[2]);
if (Number.isInteger(arg1)) {
  for (i = 0; i < arg1; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
