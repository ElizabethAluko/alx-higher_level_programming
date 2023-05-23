#!/usr/bin/node

const axios = require('axios');

// Check if a URL is provided as an argument
if (process.argv.length < 3) {
  console.log('Please provide a URL as an argument.');
  process.exit(1);
}

// Get the URL from the command line argument
const url = process.argv[2];

// Make the GET request
axios.get(url)
  .then(response => {
    console.log(`code: ${response.status}`);
  })
  .catch(error => {
    console.error(`An error occurred while making the request: ${error.message}`);
  });
