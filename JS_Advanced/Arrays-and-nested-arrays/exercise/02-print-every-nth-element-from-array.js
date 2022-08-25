function solve(array, num) {
    let newArr = []
    for (let index = 0; index < array.length; index+=num) {
        const element = array[index];
        newArr.push(element)
    }
    return newArr
}

result = solve(['5',
    '20',
    '31',
    '4',
    '20'],
    2
)

console.log(result);