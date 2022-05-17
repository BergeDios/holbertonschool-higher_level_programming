#!/usr/bin/node
// Script that returns a dictionary with a count foe every user completed tasks

const axios = require('axios').default;
const respDict = {};
axios.get(process.argv[2])
  .then((response) => {
    const json = response.data;
    // iterate through body response
    for (let i = 0; i < json.length; i++) {
      // if task completed
      if (json[i].completed === true) {
        // checl if user already has an entry in dictionary
        if (respDict[json[i].userId] === undefined) {
          respDict[json[i].userId] = 0;
        }
        // add 1
        respDict[json[i].userId] += 1;
      }
    }
    console.log(respDict);
  })
  .catch((error) => {
    console.log(error);
  })
  .then(() => {
  });
