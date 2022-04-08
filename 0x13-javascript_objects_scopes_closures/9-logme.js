#!/usr/bin/node
let argsprinted = 0;

exports.logMe = function (item) {
  console.log(argsprinted + ': ' + item);
  argsprinted++;
};
