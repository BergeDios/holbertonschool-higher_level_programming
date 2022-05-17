#!/usr/bin/node
// Script that prints every character for a star wars movie of given id

const axios = require('axios').default;
axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then((response) => {
    const characters = response.data.characters;
    for (let i = 0; i < characters.length; i++) {
      const axioschar = require('axios').default;
      axioschar.get(characters[i])
        .then((resp) => {
          console.log(resp.data.name);
        });
    }
  })
  .catch((error) => {
    console.log(error);
  })
  .then(() => {
  });
