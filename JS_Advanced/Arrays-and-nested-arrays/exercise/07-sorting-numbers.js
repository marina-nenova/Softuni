function solve(array) {
    let resultArr = [];
    let sortedArr = array.sort((a, b) => a - b);

    while (sortedArr.length > 0) {
        resultArr.push(sortedArr.shift(), sortedArr.pop())
    }
    return resultArr
}

result = solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56])
console.log(result);