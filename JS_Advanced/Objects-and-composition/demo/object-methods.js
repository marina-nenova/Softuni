let car = {
    model: 'BMW',
    year: 2010,
    facelift: true,
    honk: function () { // Method with function expression
        console.log('Beep beep!');
    },
    honk2: () => { // Methoid with arrow function 
        console.log('Beep beep2!');
    },
    honk3() { // Object method notation
        console.log('Beep beep3!');
    }
}

car.honk();
car.honk2();
car.honk3();

// Object as function library
function division(a, b) {
    return a / b;
}

let calc = {
    sum: function (a, b) {
        return a + b;
    },
    multiplication: (a, b) => a * b,
    subtraction(a, b) {
        return a - b;
    },
    division // same as division:division
};

console.log(calc.sum(10, 15));