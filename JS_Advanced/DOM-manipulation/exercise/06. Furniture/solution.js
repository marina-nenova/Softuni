function solve() {
  let [generateBtn, buyBtn] = document.querySelectorAll('button');
  let tableBody = document.querySelector('tbody');
  let outputFieldElement = document.querySelectorAll('textarea')[1];

  generateBtn.addEventListener('click', generate);
  buyBtn.addEventListener('click', buy);

  function generate() {
    const list = JSON.parse(document.querySelectorAll('textarea')[0].value);

    for (const furniture of list) {
      const row = document.createElement('tr');

      let imageData = document.createElement('td');
      let img = document.createElement('img');
      img.src = furniture.img;
      imageData.appendChild(img);
      row.appendChild(imageData);

      let nameData = document.createElement('td');
      let furnitureName = document.createElement('p');
      furnitureName.textContent = furniture.name;
      nameData.appendChild(furnitureName);
      row.appendChild(nameData);

      let priceData = document.createElement('td');
      let furniturePrice = document.createElement('p');
      furniturePrice.textContent = furniture.price;
      priceData.appendChild(furniturePrice);
      row.appendChild(priceData);

      let decData = document.createElement('td');
      let furnitureDec = document.createElement('p');
      furnitureDec.textContent = furniture.decFactor;
      decData.appendChild(furnitureDec);
      row.appendChild(decData);

      const inputData = document.createElement('td');
      const input = document.createElement('input');
      input.type = 'checkbox';
      inputData.appendChild(input);
      row.appendChild(inputData);

      tableBody.appendChild(row);

    }
  }
  function buy() {
    let checkBoxes = Array.from(document.querySelectorAll('input[type="checkbox"]')).filter(cb => cb.checked);

    let bought = [];
    let totalPrice = 0;
    let averageDecFactor = 0;

    for (let checkbox of checkBoxes) {
      let [name, price, decFactor] =
        checkbox.parentElement.parentElement.querySelectorAll('td p');

      bought.push(name.textContent);
      totalPrice += Number(price.textContent);
      averageDecFactor += Number(decFactor.textContent);
    }
    averageDecFactor /= bought.length;

    outputFieldElement.value =
      `Bought furniture: ${bought.join(', ')}\n` +
      `Total price: ${totalPrice.toFixed(2)}\n` +
      `Average decoration factor: ${averageDecFactor}`;

  }
}