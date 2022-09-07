function lockedProfile() {
    let buttonElements = document.querySelectorAll('.profile > button');

    for (let i = 0; i < buttonElements.length; i++) {
        const button = buttonElements[i];
        let parentDiv = button.parentElement;
        let lockedState = parentDiv.querySelector('input[value="lock"]');
        let hiddenInfoElement = parentDiv.querySelector(`div[id=user${i + 1}HiddenFields]`);

        button.addEventListener('click', () => {
            if (!lockedState.checked && button.textContent === 'Show more') {
                hiddenInfoElement.style.display = 'block';
                button.textContent = 'Hide it';
            } else if (!lockedState.checked && button.textContent === 'Hide it') {
                hiddenInfoElement.style.display = 'none';
                button.textContent = 'Show more';
            }
        })
    }
}