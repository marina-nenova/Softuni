function solve(array) {
    let sortedArray = array.sort((a, b) => a - b);
    let half = Math.ceil(array.length / 2);
    let biggerHalf = sortedArray.slice(array.length - half);
    return biggerHalf;
}

result = solve([4, 7, 2, 5])
console.log(result);