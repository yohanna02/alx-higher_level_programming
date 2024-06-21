#!/usr/bin/node
function addMeMaybe (number, func) {
  const newNumber = number++;
  func(newNumber);
}
module.exports = { addMeMaybe };
