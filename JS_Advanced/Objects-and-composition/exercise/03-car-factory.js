function solve(car) {
    let newCar = {};
    newCar.model = car.model;
    
    let engines = {
        'Small engine': { power: 90, volume: 1800 },
        'Normal engine': { power: 120, volume: 2400 },
        'Monster engine': { power: 200, volume: 3500 },
    };
    let carriages = {
        'hatchback': { type: 'hatchback', color: car.color },
        'coupe': { type: 'coupe', color: car.color }
    };
    
    
    if (car.power <= 90) {
        newCar.engine = engines['Small engine'];
    } else if (car.power <= 120) {
        newCar.engine = engines['Normal engine'];
    } else {
        newCar.engine = engines['Monster engine'];
    }

    newCar.carriage = carriages[car.carriage];
    
    let newWheelSize = car.wheelsize

    if (car.wheelsize % 2 === 0) {
        newWheelSize--;
    }
    newCar.wheels = new Array(4).fill(newWheelSize);

    return newCar;

}

console.log(solve({
    model: 'VW Golf II',
    power: 90,
    color: 'blue',
    carriage: 'hatchback',
    wheelsize: 14
}
));