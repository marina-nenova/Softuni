function solve(a, b) {
    let firstNumber = Number(a);
    let secondNumber = Number(b);

    while (firstNumber !== secondNumber) {
        if (firstNumber > secondNumber) {
            firstNumber -= secondNumber;
        } else {
            secondNumber -= firstNumber;
        }
    }console.log(firstNumber);

}
solve(15, 5)