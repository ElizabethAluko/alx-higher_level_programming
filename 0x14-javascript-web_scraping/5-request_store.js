#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if the URL and file path are provided as arguments
if (process.argv.length < 4) {
  console.log('Please provide the URL and file path as arguments.');
  process.exit(1);
}

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make the request to fetch the webpage contents
request.get(url, (error, response, body) => {
  if (error) {
    console.error(`An error occurred while making the request: ${error.message}`);
  } else {
    if (response.statusCode === 200) {
      // Write the body contents to the file
      fs.writeFile(filePath, body, 'utf-8', (error) => {
        if (error) {
          console.error(`An error occurred while writing to the file: ${error}`);
        } else {
          console.log(`Successfully saved the webpage contents to ${filePath}`);
        }
      });
    } else {
      console.error(`Failed to fetch the webpage. Status code: ${response.statusCode}`);
    }
  }
});
