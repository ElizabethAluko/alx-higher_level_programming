#!/usr/bin/node

const myVar = parseInt(process.argv[2]);

if (process.argv.length < 3 || isNaN(myVar)) {
  console.log('Not a number');
} else {
  console.log('My number: '.concat(myVar));
}
