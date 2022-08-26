function solve(array) {
    let sum = array[0].reduce((a, b) => a + b);

    for (let i = 0; i < array[0].length; i++) {
        
        let colSum = 0;
        
        for (let j = 0; j < array.length; j++) {
            colSum += array[j][i];
        }
        if (colSum !== sum) {
            return false;
        }
    }
    return true;
}

result = solve([[4, 5, 6],
[6, 5, 4],
[5, 5, 5]]
)

console.log(result);