function toggle() {
    let textElement = document.getElementsByClassName('button')[0];
    let moreInfo = document.getElementById('extra');
    if (textElement.textContent === 'More') {
        moreInfo.style.display = 'block';
        textElement.textContent = 'Less'
    } else if (textElement.textContent === 'Less') {
        moreInfo.style.display = 'none';
        textElement.textContent = 'More'
    }
}