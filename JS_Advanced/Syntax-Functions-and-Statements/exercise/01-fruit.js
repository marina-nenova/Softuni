function solve(fruit, weight, price) {
    let fruitType = fruit
    let weightInGrams = weight
    let fruitPrice = price
    let weightInKilos = weightInGrams / 1000
    let moneyNeeded = weightInKilos * fruitPrice

    console.log(`I need $${moneyNeeded.toFixed(2)} to buy ${weightInKilos.toFixed(2)} kilograms ${fruitType}.`);
}
solve('orange', 2500, 1.80)