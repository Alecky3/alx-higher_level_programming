#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(parseInt(num)));
}

function factorial (n) {
  if (n <= 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
