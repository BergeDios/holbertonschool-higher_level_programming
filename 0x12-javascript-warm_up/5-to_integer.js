#!/usr/bin/node
const args = process.argv;
const pnum = parseInt(args[2]);
if (isNaN(pnum)) {
  console.log('Not a number');
} else {
  console.log('My Number: '.concat(pnum));
}
