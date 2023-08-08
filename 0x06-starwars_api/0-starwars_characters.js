#!/usr/bin/node
const request = require('request');

function getMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error fetching movie data for ID ${movieId}:`, error);
      return;
    }

    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      characters.forEach(characterUrl => {
        request(characterUrl, (characterError, characterResponse, characterBody) => {
          if (characterError) {
            console.error(`Error fetching character data for URL ${characterUrl}:`, characterError);
            return;
          }

          if (characterResponse.statusCode === 200) {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
          } else {
            console.error(`Error fetching character data for URL ${characterUrl}: Status ${characterResponse.statusCode}`);
          }
        });
      });
    } else {
      console.error(`Error fetching movie data for ID ${movieId}: Status ${response.statusCode}`);
    }
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <movie_id>');
} else {
  const movieId = process.argv[2];
  getMovieCharacters(movieId);
}
