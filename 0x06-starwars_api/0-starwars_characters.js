#!/usr/bin/node
const originalRequest = require('request');
const util = require('node:util');
const argv = process.argv;
const request = util.promisify(originalRequest);

async function getMovieChars (url) {
  const res = await request(url);
  const data = JSON.parse(res.body);
  return data.characters;
}

async function main () {
  if (argv.length < 3) {
    return;
  }
  const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;
  const chars = await getMovieChars(url);

  for (const char of chars) {
    const res = await request(char);
    const charData = JSON.parse(res.body);
    console.log(charData.name);
  }
}

main();
