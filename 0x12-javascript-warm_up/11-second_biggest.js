#!/usr/bin/node

const basket = process.argv;

if (basket.length <= 3) {
  console.log(0);
} else {
  basket.sort((a, b) => a - b);
  const Second = basket[basket.length - 2];
  console.log(Number(Second));
}
