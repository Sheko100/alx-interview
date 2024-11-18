#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

request(url, function(err, res, body) {
    const data = JSON.parse(body);
    const chars = data.characters;

    for (let i = 0; i < chars.length; i++) {
        request(chars[i], function(err, res, body) {
            const charData = JSON.parse(body);
            console.log(charData.name);
        });
    }
});
