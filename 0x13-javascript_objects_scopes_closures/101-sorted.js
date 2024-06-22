#!/usr/bin/node
const { dict } = require('./101-data.js');
const newDict = {};
for (const key in dict) {
  newDict[dict[key]] = [].concat(newDict[dict[key]] || [], [key]);
}
console.log(dict);
console.log(newDict);
