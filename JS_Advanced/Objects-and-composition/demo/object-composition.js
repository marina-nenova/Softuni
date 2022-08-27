let car = {
    model: 'BMW',
    year: 2010,
    facelift: true,
    honk: function () {
        console.log(`${this.model}: Beep beep!`);
    },
    owner: {
        name: 'Pesho',
        age: 30,
    }
};

// car['honk']();

// Print nested value
console.log(car.owner.name);
console.log(car.owner['name']);
console.log(car['owner']['name']);

// Nested destructuring
let { owner } = car;

// Renaming in destructuring
let { owner: person } = car;


