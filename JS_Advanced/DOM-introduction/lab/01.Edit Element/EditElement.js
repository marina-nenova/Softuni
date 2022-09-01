function editElement(element, match, replacement) {
    let textElement = element.textContent;
    while (textElement.includes(match)) {
        textElement = textElement.replace(match, replacement);
    }
    element.textContent = textElement;
}