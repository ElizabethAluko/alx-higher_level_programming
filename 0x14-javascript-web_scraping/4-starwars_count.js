#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length < 3) {
  console.log('Please provide the API URL as an argument.');
  process.exit(1);
}

// Get the API URL from the command line argument
const apiUrl = process.argv[2];

// Define the character ID for Wedge Antilles
const characterId = 18;

// Make the API request to fetch all movies
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`An error occurred while making the API request: ${error.message}`);
  } else {
    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      const moviesWithWedgeAntilles = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
      console.log(moviesWithWedgeAntilles.length);
    } else {
      console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
    }
  }
});
