function solve() {

  function camelize(str) {

    let stringResult = '';

    for (let i = 0; i < str.length; i++) {
      if (str[i] === ' ') {
        stringResult += (str[i + 1].toUpperCase());
        i++;
      } else {
        stringResult += str[i];
      }
    }
    return stringResult;
  }

  function pascalize(str) {

    let stringResult = '';
    stringResult += str[0].toUpperCase();

    for (let i = 1; i < str.length; i++) {
      if (str[i] === ' ') {
        stringResult += (str[i + 1].toUpperCase());
        i++;
      } else {
        stringResult += str[i];
      }
    }
    return stringResult;
  }

  let input = document.getElementById('text').value;
  let currentCase = document.getElementById('naming-convention').value;

  let textLower = input.toLowerCase()

  let result = '';

  if (currentCase === "Camel Case") {
    result = camelize(textLower);
  } else if (currentCase === "Pascal Case") {
    result = pascalize(textLower);
  } else {
    result = 'Error!'
  }

  let resultElement = document.getElementById('result');

  resultElement.textContent = result;
}