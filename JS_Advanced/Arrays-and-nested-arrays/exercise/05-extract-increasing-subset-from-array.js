function solve(array) {
    let biggestNum = array[0];
    let newArr = []

    for (const num of array) {
        if (num >= biggestNum) {
            newArr.push(num);
            biggestNum = num;
        }
    }
    console.log(newArr);
}

solve([1,
    3,
    8,
    4,
    10,
    12,
    3,
    2,
    24]
)