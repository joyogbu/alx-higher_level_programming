#!/usr/bin/node
const arg = process.argv;
arg1 = Number(arg[2]);
function factorial(n) {
  if (isNaN(arg1)) {
    return 1;
  }
  if (n == 0 || n == 1) {
    return 1;
  } else {
      return n * factorial(n - 1);
    }
}
console.log(factorial(arg1));
