function addItem() {
    let itemsElement = document.getElementById('items');
    let inputTextElement = document.getElementById('newItemText')

    let newLiElement = document.createElement('li');
    newLiElement.textContent = inputTextElement.value;

    let deleteLinkElement = document.createElement('a')
    deleteLinkElement.href = '#';
    deleteLinkElement.textContent = '[Delete]'

    deleteLinkElement.addEventListener('click', function (el) {
        el.currentTarget.parentNode.remove();
    })

    newLiElement.appendChild(deleteLinkElement);

    itemsElement.appendChild(newLiElement);
    inputTextElement.value = '';
}