#!/usr/bin/node
const noArgs = process.argv;
if (noArgs.length <= 2) {
  console.log('No argument');
} else if (noArgs.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
