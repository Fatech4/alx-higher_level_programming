#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
// First request
request(`${apiUrl}`, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid API response:', response.statusCode);
    return;
  }

  const films = JSON.parse(body).results;
  const film = films[id - 1];
  film.characters.forEach(character => {
  // Second request inside the callback of the first request
    request(character, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Invalid API response:', response.statusCode);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
