let cars = ['BMW', 'audi', 'Opel'];
let oldCars = ['Lada', 'Moskvich', 'Volga'];

// Join
let stringResult = cars.join(', ');
console.log(stringResult);

// Concat
let allCars = cars.concat(oldCars);
console.log(allCars);

// Slice
let slicedCars = allCars.slice(2, 4);
let slicedOldCars = allCars.slice(3);
let clonedAllCars = allCars.slice(); // Note: easy way to clone array
console.log(slicedCars);
console.log(slicedOldCars);
console.log(clonedAllCars);

// Includes
let isAvailable = allCars.includes('Lada');
console.log(isAvailable);

// IndexOf
let ladaIndex = allCars.indexOf('Lada');
console.log(ladaIndex);
let trabantIndex = allCars.indexOf('Trabant');  // Car not found
console.log(trabantIndex);
