#!/usr/bin/node
function nbOccurences (arr, item) {
  let occurence = 0;
  arr.forEach(function (a) {
    if (a === item) occurence++;
  });
  return occurence;
}
module.exports = { nbOccurences };
