function extractText() {
    let listitems = document.getElementById('items')
    let textElements = listitems.textContent;

    let resultElement = document.getElementById('result');
    resultElement.textContent = textElements;
}