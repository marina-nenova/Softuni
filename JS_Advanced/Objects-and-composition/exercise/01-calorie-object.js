function solve(array) {
    let calorieObject = {}

    for (let index = 0; index < array.length; index+=2) {
        let foodName = array[index]
        let foodCalories = array[index + 1]
        calorieObject[foodName] = Number(foodCalories)
    }
    console.log(calorieObject);
}

solve(['Yoghurt', '48', 'Rise', '138', 'Apple', '52'])