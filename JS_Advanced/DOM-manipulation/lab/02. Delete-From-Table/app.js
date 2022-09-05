function deleteByEmail() {
    let emailInputElement = document.querySelector('input[name="email"]');
    let resultElement = document.getElementById('result');

    let emailCellElements = document.querySelectorAll('tr td:nth-of-type(2)');
    let emailElements = Array.from(emailCellElements);

    let targetElement = emailElements.find(x => x.textContent == emailInputElement.value)

    if (targetElement) {
        targetElement.parentNode.remove()
        resultElement.textContent = 'Deleted.'
    } else {
        resultElement.textContent = 'Not found.'
    }
    emailInputElement.value = ''
}