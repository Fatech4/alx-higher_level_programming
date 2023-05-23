#!/usr/bin/node
const id = process.argv[2];
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${id}`,
  (error, response, body) => {
    if (error) {
      console.error(error);
    }
    console.log(JSON.parse(body).title);
  });
