function solve(array) {
    let oddPos = []
    for (let i = 0; i < array.length; i++) {
        if (i % 2 !== 0) {
            let element = array[i] * 2;
            oddPos.push(element)
        }
    }
    return oddPos.reverse().join(' ')
}

result = solve([10, 15, 20, 25])
console.log(result);