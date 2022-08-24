let cars = ['BMW', 'audi', 'Opel', 'Lada', 'Moskvich', 'Volga'];

// For of loop
for (let car of cars) {
    // console.log(car);
}

// forEach Method!
cars.forEach((car) => {
    console.log(car);
});

// Some
let result = cars.some((car) => {
    return car[0] == 'V';
});
console.log(result);

// Find
let longNameCar = cars.find((car) => {
    return car.length > 4;
});

console.log(longNameCar);

// Filter
let fourLetterCars = cars.filter(car => car.length == 4);

console.log(fourLetterCars);

// Map
let numbers = [1, 2, 3, 4, 5];
let doubledNumbers = numbers.map(num => num * 2);
console.log(numbers);
console.log(doubledNumbers);
let upperCaseCars = cars.map(car => car.toUpperCase());
console.log(upperCaseCars);

// Reduce
let sum = numbers.reduce((acc, num) => {
    return acc + num;
}, 0);

console.log(sum);

// Nested arrays
let arr = [
    [1, 2, 3], 
    [2, 3, 4], 
    [6, 45, 3, 10]
];

console.log(arr[1][1]);