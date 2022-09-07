function attachEventsListeners() {
    let [inputField, outputField] = document.querySelectorAll('input[type="text"]');
    let buttonElement = document.getElementById('convert');

    let inputUnits = document.getElementById('inputUnits');
    let outputUnits = document.getElementById('outputUnits');

    let rations = {
        km: 1000,
        m: 1,
        cm: 0.01,
        mm: 0.001,
        mi: 1609.34,
        yrd: 0.9144,
        ft: 0.3048,
        in: 0.0254
    }

    function convertUnits() {
        let convertValue = Number(inputField.value);
        let fromValue = inputUnits.value;
        let toValue = outputUnits.value;
        let convertValueInMeters = convertValue * rations[fromValue];

        result = convertValueInMeters / rations[toValue];
        outputField.value = result;
    }

    buttonElement.addEventListener('click', convertUnits);
}

