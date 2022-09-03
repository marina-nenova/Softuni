function generateReport() {
    let checkBoxes = document.querySelectorAll('input')

    let cbIndices = [];

    for (let index = 0; index < checkBoxes.length; index++) {
        const element = checkBoxes[index];
        if (element.checked) {
            cbIndices.push(index);
        }
    }
    let rows = document.getElementsByTagName('tr');
    rowsArr = Array.from(rows);
    rowsArr.shift();

    let result = [];

    for (let row of rowsArr) {
        let info = {};
        for (let index of cbIndices) {
            let name = checkBoxes[index].name;
            let rowIinfo = row.children[index].textContent;
            info[name] = rowIinfo;
        }
        result.push(info)
    }
    report = JSON.stringify(result);

    let outputElement = document.getElementById('output');
    outputElement.textContent = report;

}