function solve(array) {
    let numArr = [];
    let result = 0;

    for (let index = 0; index < array.length; index++) {
        let command = array[index];
        result += 1;
        if (command === 'add') {
            numArr.push(result);
        } else if (command === 'remove') {
            numArr.pop();
        }

    }
    if (numArr.length === 0) {
        console.log('Empty');
    } else {
        numArr.forEach(element => {
            console.log(element);
        });
    }
}

solve(['add',
    'add',
    'remove',
    'add',
    'add']
)