#!/usr/bin/node
const numbers = process.argv;
let biggest = parseInt(numbers[2]);
let secondBiggest = parseInt(numbers[2]);
if (numbers.length <= 3) {
  console.log(0);
} else {
  for (let i = 0; i < numbers.length - 2; i++) {
    const number = parseInt(numbers[i + 2]);
    if (number > biggest) {
      secondBiggest = biggest;
      biggest = number;
    } else if (number !== biggest && number > secondBiggest) {
      secondBiggest = number;
    }
  }
  console.log(secondBiggest);
}
