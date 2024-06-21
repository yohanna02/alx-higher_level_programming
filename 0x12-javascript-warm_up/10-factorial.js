#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 1 || n === 0) {
    return 1;
  } else if (n < 0) {
    return n;
  }

  return n * factorial(n - 1);
}
const answer = factorial(parseInt(process.argv[2]));
console.log(answer);
