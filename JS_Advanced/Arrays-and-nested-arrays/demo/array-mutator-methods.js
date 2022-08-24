let cars = ['BMW', 'audi', 'Opel'];

// Pop
let lastElement = cars.pop();
console.log(lastElement);
console.log(cars);

// Push cars[cars.lengt] = 'Mercedess'
// let newLength = cars.push('Mercedess', ''Honda');
let newLength = cars.push('Mercedess');
console.log(newLength);
console.log(cars);

// Shift
let firstElement = cars.shift();
console.log(firstElement);
console.log(cars);

// Unshift
newLength = cars.unshift('Honda');
console.log(cars);

// Splice
cars.splice(1, 0, 'BWM', 'Hundai');
console.log(cars);
let deletedCars = cars.splice(2, 1);
console.log(deletedCars);
console.log(cars);
// cars.splice(2, 1, 'Hundai');
// console.log(cars);

// Fill
// let numbers = [];
// numbers.length = 10;
// numbers.fill(0);
// console.log(numbers);

// Reverse
cars.reverse();
console.log(cars);

// Sort
cars.sort()
console.log(cars);
let numbers = [9, 10, 6, 3];
console.log(numbers.sort());

// Number sort
// numbers.sort(function (a, b) {
//     if (a < b) {
//         return -1
//     } else if (a > b) {
//         return 1;
//     } else {
//         return 0
//     }
// });

numbers.sort((a, b) => a - b);

console.log(numbers);

// Alphabetical sort
cars.sort((a, b) => a.localeCompare(b));
console.log(cars);