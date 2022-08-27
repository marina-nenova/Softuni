let car = {
    model: 'BMW',
    year: 2010,
    facelift: true,
    honk: function () {
        console.log(`${this.model}: Beep beep!`);
    },
};

car.honk();
car.model = 'Mercedess';
car.honk();

// Change execution context
let singleHonk = car.honk;

singleHonk();

let russianMachine = {
    model: 'Lada'
}

russianMachine.bibitka = car.honk;

russianMachine.bibitka();