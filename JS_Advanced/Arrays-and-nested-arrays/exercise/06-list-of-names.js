function solve(array) {
    let sortedArr = array.sort((a, b) => a.localeCompare(b));
    let orderNum = 1;

    sortedArr.forEach(element => {
        console.log(`${orderNum}.${element}`);
        orderNum++;
    });
}

solve(["John", "Bob", "Christina", "Ema"])