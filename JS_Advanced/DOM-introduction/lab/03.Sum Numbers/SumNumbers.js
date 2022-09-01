function calc() {
    let num1 = document.getElementById('num1');
    let num2 = document.getElementById('num2');

    console.log(typeof num1);

    let sum = Number(num1.value) + Number(num2.value);

    let resultElement = document.getElementById('sum')
    resultElement.value = sum;
}
