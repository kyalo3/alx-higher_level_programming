#!/usr/bin/node

const length = process.argv.length;

length === 2 ? console.log('No argument') : length === 3 ? console.log('Argument found') : console.log('Arguments found');
