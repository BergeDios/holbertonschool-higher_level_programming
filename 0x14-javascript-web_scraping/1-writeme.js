#!/usr/bin/node
// Script that writes text to a file given parameters in args 2 and 3
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], err => {
  if (err) {
    console.error(err);
  }
});
