// Function declaration
function printFullName(firstName, lastName) {
    console.log(firstName + ' ' + lastName);
}

// Function invokation
printFullName('Peter', 'Ivanov');
printFullName('Peter', 'Petrov');
printFullName('Ivan', 'Ivanov');

// Function expression
let countDown = function(number = 10) {
    for (let i = number; i > 0; i--) {
        console.log(i);
    }
}

countDown(11);

// Arrow function
let countUp = (max) => {
    for (let i = 0; i < max; i++) {
        console.log(i);
    }
};

countUp(10);


// Return value
function sum(a, b) {
    return a + b;
}

let sumArrow = (a, b) => a + b;

let result = sum(1, 3);
console.log(result);

// Method
let firstName = 'Pesho';
console.log(firstName.toUpperCase());
console.log(Math.PI);