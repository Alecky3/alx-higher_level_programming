#!/usr/bin/node
const noArgs = process.argv;
const arg = noArgs[2];
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
