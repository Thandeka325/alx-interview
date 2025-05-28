#!/usr/bin/node
/* Prints all characters of a Star Wars movie in order using the SWAPI */

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  const printCharacter = (index) => {
    if (index >= characters.length) return;

    request(characters[index], (charErr, charRes, charBody) => {
      if (charErr) {
        console.error(charErr);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
      printCharacter(index + 1);
    });
  };

  printCharacter(0);
});
