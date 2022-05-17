#!/usr/bin/node
// Script that checks for a specific character via id in every movie and counts
const axios = require('axios').default;
let counter = 0;
const target = 'https://swapi-api.hbtn.io/api/people/18/';

axios.get(process.argv[2])
  .then((response) => {
    const results = response.data.results;
    // iterate through movies in the result key to search in their characters
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      // iterate through characters if target found num_films +1
      for (let j = 0; j < characters.length; j++) {
        if (characters[j] === target) {
          counter += 1;
        }
      }
    }
    console.log(counter);
  })
  .catch((error) => {
    console.log(error);
  })
  .then(() => {
  });
