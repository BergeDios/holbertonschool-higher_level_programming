#!/usr/bin/node
// Sxcript sends get request to webpage and stores respones in a file given
const axios = require('axios').default;
axios.get(process.argv[2])
  .then((response) => {
    const filename = process.argv[3];
    const responseText = response.data;
    const fs = require('fs');
    fs.writeFile(filename, responseText, err => {
      if (err) {
        console.log(err);
      }
    });
  });
