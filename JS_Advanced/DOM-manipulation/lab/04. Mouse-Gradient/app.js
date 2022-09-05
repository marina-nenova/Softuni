function attachGradientEvents() {
    let gradientElement = document.getElementById('gradient');
    let resultElement = document.getElementById('result');

    gradientElement.addEventListener('mousemove', (e) => {
        let maxWidth = e.target.clientWidth;
        let mousePosition = e.offsetX;

        let percentage = Math.floor((mousePosition / maxWidth) * 100);
        resultElement.textContent = `${percentage}%`
    })
}