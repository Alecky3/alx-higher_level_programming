#!/usr/bin/node
const myArgs = process.argv;
if (myArgs.length <= 2) {
  console.log(0);
} else if (myArgs.length === 3) {
  console.log(0);
} else {
  myArgs.sort();
  console.log(myArgs[myArgs.length - 2]);
}
