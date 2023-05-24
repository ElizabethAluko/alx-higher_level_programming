#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  const moviesWithWedgeAntilles = (!error && response.statusCode === 200) ? JSON.parse(body).results.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) : [];
  console.log(moviesWithWedgeAntilles.length);
});
