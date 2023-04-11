#!/usr/bin/node

const myVar1 = process.argv[2];
const myVar2 = process.argv[3];

if (myVar1 >= 3) {
  console.log(myVar1.concat(' is ', myVar2));
} else {
  console.log('undefined'.concat(' is ', myVar2));
}
