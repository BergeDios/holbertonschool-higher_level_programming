#!/usr/bin/node
// Script that displays the status code of a GET request
const axios = require('axios').default;
axios.get(process.argv[2])
  .then((response) => {
    // handle success
    console.log('code: ' + response.status);
  })
  .catch((error) => {
    // handle error
    console.log('code: ' + error.response.status);
  })
  .then(() => {
  });
