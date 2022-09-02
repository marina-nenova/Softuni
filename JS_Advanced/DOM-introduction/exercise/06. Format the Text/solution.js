function solve() {
  let input = document.getElementById('input');

  let inputArr = input.value.split('.').filter(s => s !== '');

  let resultDiv = document.getElementById('output');

  while (inputArr.length > 0) {
    let text = inputArr.splice(0, 3).join(". ") + '.';
    let p = document.createElement('p');
    p.textContent = text;
    resultDiv.appendChild(p);
  }
}