#!/usr/bin/node
// Script that prints every character for a star wars movie of given id

const axios = require('axios').default;
// get request to star wars api
axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then((response) => {
    // with response save character list in variable
    const characters = response.data.characters;
    // iterate over it creating new requests to get name
    for (let i = 0; i < characters.length; i++) {
      const axioschar = require('axios').default;
      // new axios to get request with each character
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
