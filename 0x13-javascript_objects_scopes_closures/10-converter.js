#!/usr/bin/node

function toBinary (number) {
  return number.toString(2);
}

function toOctal (number) {
  return number.toString(8);
}

function toHexadecimal (number) {
  return number.toString(16);
}

function converter (base) {
  switch (base) {
    case 2:
      return toBinary;
    case 8:
      return toOctal;
    case 16:
      return toHexadecimal;
  }
}
module.exports = { converter };
