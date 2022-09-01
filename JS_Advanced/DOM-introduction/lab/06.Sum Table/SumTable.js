function sumTable() {
    let rowElements = document.querySelectorAll('tr td:nth-of-type(2)');

    let sum = Array.from(rowElements).reduce((a, x) => {
        let currentElement = Number(x.textContent) || 0;
        return a + currentElement;
    }, 0)

    let sumElement = document.getElementById('sum')
    sumElement.textContent = sum
}