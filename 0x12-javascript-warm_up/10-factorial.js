#!/usr/bin/node
const args = process.argv.slice(2);
const pnum = parseInt(args[0]);
function factorial (a) {
  if (isNaN(a) || a === 0) {
    return (1);
  }
  if (a > 0) {
    return (a * factorial(a - 1));
  }
}
console.log(factorial(pnum));
