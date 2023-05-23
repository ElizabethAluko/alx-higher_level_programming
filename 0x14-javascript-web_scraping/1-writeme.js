#!/usr/bin/node

const fs = require('fs');

function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (error) => {
    if (error) {
      console.error(`An error occurred while writing to the file: ${error}`);
    }
  });
}

// Check if file path and content are provided as arguments
if (process.argv.length < 4) {
  console.log('Please provide a file path and content as arguments.');
  process.exit(1);
}

// Get the file path and content from the command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the content to the file
writeToFile(filePath, content);
