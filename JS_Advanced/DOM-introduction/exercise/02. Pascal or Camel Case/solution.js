function solve() {
  function camelize(str) {
    return str.replace(/(?:^\w|[A-Z]|\b\w|\s+)/g, function (match, index) {
      if (+match === 0) return ""; // or if (/\s+/.test(match)) for white spaces
      return index === 0 ? match.toLowerCase() : match.toUpperCase();
    });
  }

  let input = document.getElementById('text').value;
  let currentCase = document.getElementById('naming-convention').value;

  let textLower = input.toLowerCase()

  let result = '';

  if (currentCase === "Camel Case") {
    result = camelize(textLower);
  } else if (currentCase === "Pascal Case") {
    const toPascalCase = str => (str.match(/[a-zA-Z0-9]+/g) || []).map(w => `${w.charAt(0).toUpperCase()}${w.slice(1)}`).join('');
    result = toPascalCase(textLower);
  } else {
    result = 'Error!'
  }

  let resultElement = document.getElementById('result');

  resultElement.textContent = result;
}