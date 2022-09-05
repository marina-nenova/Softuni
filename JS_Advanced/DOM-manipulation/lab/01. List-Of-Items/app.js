function addItem() {
    let itemsElement = document.getElementById('items');
    let inputTextElement = document.getElementById('newItemText');

    let newLiElement = document.createElement('li');
    newLiElement.textContent = inputTextElement.value;

    itemsElement.appendChild(newLiElement);
    inputTextElement.value = '';
}