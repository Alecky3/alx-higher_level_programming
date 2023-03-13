#!/usr/bin/node
let noArgs = process.argv;
let arg = noArgs[2];
if (arg === undefined) {
	console.log("No argument");
} else {
	console.log(arg);
}
