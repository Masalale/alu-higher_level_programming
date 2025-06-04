#!/usr/bin/node

const file = require('file');
const filePath = process.argv[2];

file.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
