#!/usr/bin/node
if (process.agrv.length < 3) {
  console.log('No argument');
} else if (process.argv.length >= 3) {
  console.log('Argument found');
}
