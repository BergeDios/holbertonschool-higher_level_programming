#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    if (isNaN(parseInt(args[i])) === false) {
      args[i] = parseInt(args[i]);
    }
    args.sort((a, b) => a - b);
  }
  console.log(args);
  console.log(args[(args.length - 2)]);
}
