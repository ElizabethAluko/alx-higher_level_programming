#!/usr/bin/node

const fs = require('fs');

function readFile(filePath) {
  fs.readFile(filePath, 'utf-8', (error, content) => {
    if (error) {
      console.error(`An error occurred while reading the file: ${error}`);
    } else {
      console.log(content);
    }
  });
}

// Check if a file path is provided as an argument
if (process.argv.length < 3) {
  console.log("Please provide a file path as an argument.");
  process.exit(1);
}

// Get the file path from the command line argument
const filePath = process.argv[2];

// Read and print the content of the file
readFile(filePath);
