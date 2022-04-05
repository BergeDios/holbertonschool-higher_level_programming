#!/usr/bin/node
const array = require('./100-data.js').list;
console.log(array);
const array2 = array.map((x, index) => x * index);
console.log(array2);
