function solve(array) {
    let newArray = []
    for (const el of array) {
        if (el >= 0) {
            newArray.push(el);
        } else {
            newArray.unshift(el);
        }
    }
    for (const num of newArray) {
        console.log(num);
    }

}

solve([3, -2, 0, -1])
