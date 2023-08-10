#!/usr/bin/node

const request = require('request');

function getMovieCharacters (movieId) {
  const baseUrl = 'https://swapi.dev/api/';

  request(`${baseUrl}films/${movieId}/`, (error, response, filmBody) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const filmData = JSON.parse(filmBody);
    const characters = filmData.characters;

    // Fetch and display character names
    characters.forEach(characterUrl => {
      request(characterUrl, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          console.error('Error:', characterError);
          return;
        }

        const characterData = JSON.parse(characterBody);
        console.log(characterData.name);
      });
    });
  });
}

const args = process.argv.slice(2); // Get command-line arguments
const movieId = args[0];

if (!movieId) {
  console.error('Usage: node 0-starwars_characters.js <movieId>');
} else {
  getMovieCharacters(movieId);
}
