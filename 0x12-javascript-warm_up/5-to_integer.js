#!/usr/bin/node
const args = process.argv.slice(2);
const pnum = parseInt(args[0]);
if (isNaN(pnum)) {
  console.log('Not a number');
} else {
  console.log('My Number: '.concat(pnum));
}
