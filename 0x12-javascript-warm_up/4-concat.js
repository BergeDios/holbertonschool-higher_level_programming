#!/usr/bin/node
{
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.log('undefined is undefined');
  } else if (args.length === 1) {
    const result = args[0].concat(' is undefined');
    console.log(result);
  } else {
    const result2 = args[0].concat(' is ', args[1]);
    console.log(result2);
  }
}
