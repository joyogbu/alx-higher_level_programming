#!/usr/bin/node
const arg = process.argv;
let myStr = '';
let i;
let j;
const arg1 = Number(arg[2]);
if (Number.isInteger(arg1)) {
  for (i = 0; i < arg1; i++) {
    for (j = 0; j < arg1; j++) {
      myStr += 'X';
    }
    if (i <= arg1) {
      myStr += '\n';
    }
  }
  console.log(myStr);
} else {
  console.log('Missing size');
}
