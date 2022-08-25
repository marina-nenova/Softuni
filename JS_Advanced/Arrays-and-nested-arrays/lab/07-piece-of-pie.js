function solve(array, p1, p2) {
    let startIndex = array.indexOf(p1);
    let endIndex = array.indexOf(p2)
    let result = array.slice(startIndex, endIndex + 1);
    return result
}

result = solve(['Apple Crisp',
'Mississippi Mud Pie',
'Pot Pie',
'Steak and Cheese Pie',
'Butter Chicken Pie',
'Smoked Fish Pie'],
'Pot Pie',
'Smoked Fish Pie'
)

console.log(result);