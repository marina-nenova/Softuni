function solve(array) {
    let rightDiagonalSum = 0;
    let leftDiagonalSum = 0;
    for (let index = 0; index < array.length; index++) {
        rightDiagonalSum += array[index][index]
        leftDiagonalSum += array[index][array.length - 1 - index]
    }
    console.log(`${rightDiagonalSum} ${leftDiagonalSum}`);
}

solve([[3, 5, 17],
[-1, 7, 14],
[1, -8, 89]]
)