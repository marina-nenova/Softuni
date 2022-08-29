function solve(array) {
    let result = [];
    
    for (let i = 1; i < array.length; i++) {
        let currentInfo = array[i].split('|');
        let name = currentInfo[1].trim();
        let lattitude = Number(currentInfo[2].trim()).toFixed(2);
        let longitude = Number(currentInfo[3].trim()).toFixed(2);

        let town = {"Town": name, "Latitude": Number(lattitude), "Longitude": Number(longitude)};
        result.push(town);
    }
    let jsonOutput = JSON.stringify(result);
    console.log(jsonOutput);
}

solve(['| Town | Latitude | Longitude |',
    '| Sofia | 42.696552 | 23.32601 |',
    '| Beijing | 39.913818 | 116.363625 |']
)