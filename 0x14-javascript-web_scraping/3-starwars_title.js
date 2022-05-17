#!/usr/bin/node
// Script that uses the Star Wars api to request for pages with movie id
const axios = require('axios').default;
const movieId = process.argv[2];
axios.get('http://swapi-api.hbtn.io/api/films/' + movieId)
  .then((response) => {
    console.log(response.data.title);
  })
  .catch((error) => {
    console.log(error);
  })
  .then(() => {
  });
