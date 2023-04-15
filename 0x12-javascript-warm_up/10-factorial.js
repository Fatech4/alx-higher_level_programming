#!/usr/bin/node
const arg = process.argv.splice(2, 1);
function computeFactorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (parseInt(n) <= 1) {
    return 1;
  } else {
    const factorial = parseInt(n) * computeFactorial(parseInt(n) - 1);
    return factorial;
  }
}
console.log(computeFactorial(arg[0]));
