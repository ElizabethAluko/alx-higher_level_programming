#!/usr/bin/node

const request = require('request');

// Check if a URL is provided as an argument
if (process.argv.length < 3) {
  console.log('Please provide a URL as an argument.');
  process.exit(1);
}

// Get the URL from the command line argument
const url = process.argv[2];

// Make the GET request
request.get(url, (error, response) => {
  if (error) {
    console.error(`An error occurred while making the request: ${error.message}`);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
