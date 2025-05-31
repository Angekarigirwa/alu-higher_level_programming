#!/usr/bin/node
const argument = parseInt(process.argv[2]);
if (isNaN(argument)) {
  console.log(1);
} else {
  console.log(fact(argument));
}

function fact (n) {
  if (n === 0) {
    return 1;
  }
  return n * fact(n - 1);
}
