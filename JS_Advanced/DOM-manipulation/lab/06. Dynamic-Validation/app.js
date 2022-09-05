function validate() {
    let inputElement = document.getElementById('email');
    let reg = /^([\w\-.]+)@([a-z]+)(\.[a-z]+)+$/;

    function validateEmail(event) {
        if (reg.test(event.currentTarget.value)) {
            event.target.removeAttribute('class');
            return;
        }

        event.target.className = 'error';
    }

    inputElement.addEventListener('change', validateEmail);
}