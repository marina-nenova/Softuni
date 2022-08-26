function solve(array) {
    let matrix = []
    array.forEach(element => {
        matrix.push(element.split(" ").map(Number))
    });

    let rightDiagonalSum = 0;
    let leftDiagonalSum = 0;

    for (let index = 0; index < matrix.length; index++) {
        rightDiagonalSum += matrix[index][index]
        leftDiagonalSum += matrix[index][matrix.length - 1 - index]
    }
    if (rightDiagonalSum === leftDiagonalSum) {
        for (let i = 0; i < matrix.length; i++) {
            for (let j = 0; j < matrix[i].length; j++) {
                if (j !== matrix.length - 1 - i && i !== j) {
                    matrix[i][j] = rightDiagonalSum
                }
            }
        }
    }
    matrix.forEach(el => console.log(el.join(' ')))
}


solve(['5 3 12 3 1',
    '11 4 23 2 5',
    '101 12 3 21 10',
    '1 4 5 2 2',
    '5 22 33 11 1']
)