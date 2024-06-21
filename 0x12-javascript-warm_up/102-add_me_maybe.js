#!/usr/bin/node
function addMeMaybe (number, func) {
  const newNumber = number + 1;
  func(newNumber);
}
module.exports = { addMeMaybe };
