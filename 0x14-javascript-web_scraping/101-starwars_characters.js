#!/usr/bin/node
const request = require('request');

// Check if the correct number of arguments are provided
if (process.argv.length !== 3) {
  console.log('Usage: node star_wars_characters.js <Movie ID>');
  process.exit(1);
}

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// API endpoint URL
const url = `https://swapi.dev/api/films/${movieId}`;

// Send a GET request to the Star Wars API to fetch film data
request(url, (error, response, body) => {
  if (error) {
    console.log(`An error occurred: ${error}`);
    return;
  }

  // Check if the request was successful
  if (response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    // Fetch and print the character names in order
    fetchAndPrintCharacters(characters, 0);
  } else {
    console.log(`Error: ${response.statusCode} - ${response.statusMessage}`);
  }
});

// Function to fetch and print character names in order
function fetchAndPrintCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  const characterUrl = characters[index];
  request(characterUrl, (error, response, body) => {
    if (error) {
      console.log(`An error occurred: ${error}`);
      return;
    }

    const characterData = JSON.parse(body);
    const characterName = characterData.name;
    console.log(characterName);

    // Fetch and print the next character
    fetchAndPrintCharacters(characters, index + 1);
  });
}
