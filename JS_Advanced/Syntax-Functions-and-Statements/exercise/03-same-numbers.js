function solve(number) {
    let numAsString = number.toString();
    let sameNumbers = true;
    let numToCompare = numAsString[0];
    let sumNums = 0;

    for (let index = 0; index < numAsString.length; index++) {
        let currentElement = numAsString[index];
        sumNums += Number(currentElement);
        if (currentElement !== numToCompare) {
            sameNumbers = false
        }
    }
    console.log(sameNumbers);
    console.log(sumNums);
}
solve(1234)