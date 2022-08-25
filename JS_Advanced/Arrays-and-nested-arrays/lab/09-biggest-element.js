function solve(array) {
    let maxNum = 0;


    for (let index = 0; index < array.length; index++) {
        let currentArr = array[index];
        let currentMaxNum = Math.max(...currentArr);

        if (currentMaxNum >= maxNum) {
            maxNum = currentMaxNum;
        }

    }
    return maxNum
}

result = solve([[3, 5, 7, 12],
[-1, 4, 33, 2],
[8, 3, 0, 4]]

)
console.log(result);