#!/usr/bin/node

let i, j;
let newstr = '';

if (process.argv.length <= 2) {
} else if (process.argv[2] < 0) {
  console.log();
} else {
  for (i = 0; i < process.argv[2]; i++) {
    newstr += 'X';
  }
  for (j = 0; j < process.argv[2]; j++) {
    console.log(newstr);
  }
}
