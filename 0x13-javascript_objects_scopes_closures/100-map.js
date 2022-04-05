#!/usr/bin/node
let array = require('./100-data.js').list;
console.log(array);
let array2 = [];
for (let i = 0; i < array.length; i++) {
  array2[i] = array[i] * i;
};
console.log(array2);
