#!/usr/bin/node
const args = process.argv.slice(2);
const pnum = parseInt(args[0]);
if (isNaN(pnum)) {
  console.log('Missing size');
} else {
  let string = '';
  let i = 0;
  for (i = 0; i < pnum; i++) {
    string = string + 'X';
  }
  for (let j = 0; j < pnum; j++) {
    console.log(string);
  }
}
