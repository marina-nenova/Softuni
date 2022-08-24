function solve(array) {
    let sortedNums = array.sort((a, b) => a - b);
    let smallestHalf = array.slice(0, 2);
    console.log(smallestHalf.join(" "));
}

solve([3, 0, 10, 4, 7, 3])