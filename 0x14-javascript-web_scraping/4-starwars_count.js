#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url,
  (error, response, body) => {
    if (error) {
      console.error(error);
    }
    const films = JSON.parse(body).results;
    const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
    const movieWithWedge = films.filter(film => {
      return film.characters.includes(wedgeUrl);
    });
    console.log(movieWithWedge.length);
  });
