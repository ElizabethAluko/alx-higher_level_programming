#!/usr/bin/node

const request = require('request');

// Check if a movie ID is provided as an argument
if (process.argv.length < 3) {
  console.log('Please provide a movie ID as an argument.');
  process.exit(1);
}

// Get the movie ID from the command line argument
const movieId = process.argv[2];

// Construct the API endpoint URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make the API request
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`An error occurred while making the API request: ${error.message}`);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      console.log(movie.title);
    } else {
      console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
    }
  }
});
