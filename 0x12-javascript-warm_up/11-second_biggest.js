#!/usr/bin/node
const arg = process.argv.slice(2);
let x;
if (arg.length === 0 || arg.length === 1) {
  x = 0;
} else {
  x = Math.max.apply(null, arg);
  arg.splice(arg.indexOf(x), 1);
  x = Math.max.apply(null, arg);
}
console.log(x);
