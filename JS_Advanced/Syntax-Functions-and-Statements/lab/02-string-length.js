function solve(first, second, third) {
    let firstLength = first.length;
    let secondLength = second.length;
    let thirdLength = third.length;

    let sum = firstLength + secondLength + thirdLength;
    let result = Math.floor(sum / 3);

    console.log(sum);
    console.log(result);
}
solve('chocolate', 'ice cream', 'cake')