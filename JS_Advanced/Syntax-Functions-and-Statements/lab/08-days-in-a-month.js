function solve(month, year) {
    return new Date(year, month, 0).getDate();
}

let days = solve(2, 2020);
console.log(days)