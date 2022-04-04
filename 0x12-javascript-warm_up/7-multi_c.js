#!/usr/bin/node
const args = process.argv.slice(2);
const pnum = parseInt(args[0]);
if (isNaN(pnum)) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = 0; i < pnum; i++) {
    console.log('C is fun');
  }
}
