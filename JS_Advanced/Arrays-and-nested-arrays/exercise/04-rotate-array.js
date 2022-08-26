function solve(array, num) {
    for (let index = 0; index < num; index++) {
        array.unshift(array.pop())

    }
    console.log(array.join(' '));
}

solve(['Banana',
    'Orange',
    'Coconut',
    'Apple'],
    15

)