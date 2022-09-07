function addItem() {
    let itemTextElement = document.getElementById('newItemText');
    let itemValueElement = document.getElementById('newItemValue');
    let selectElement = document.getElementById('menu');

    let optionsElement = document.createElement('option');
    
    if (itemTextElement.value && itemValueElement.value) {
        optionsElement.textContent = itemTextElement.value;
        optionsElement.value = itemValueElement.value;
        selectElement.appendChild(optionsElement);
        itemTextElement.value = '';
        itemValueElement.value = '';
    }
}