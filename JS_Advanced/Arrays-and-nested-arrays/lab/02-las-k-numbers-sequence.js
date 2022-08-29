function lastKNumbers(n, k) {

    let result = [1];

    for (let i = 1; i < n; i++) {

        let start = i - k < 0 ? 0 : i - k;
        result.push(result.slice(start).reduce((a, b) => a + b));
    }

    return result;
}
console.log(lastKNumbers(6, 3));


