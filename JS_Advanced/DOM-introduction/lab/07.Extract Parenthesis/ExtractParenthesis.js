function extract(content) {
    let textElement = document.getElementById(content);

    let pattern = /\(([^(]+)\)/g;
    let matches = textElement.textContent.matchAll(pattern);
    let result = [];

    for (const match of matches) {
        result.push(match[1]);

    }
    return result.join('; ')
}