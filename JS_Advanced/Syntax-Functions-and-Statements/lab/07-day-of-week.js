function solve(string) {
    let result;
    if (string === "Monday") {
        result = 1;
    } else if (string === "Tuesday") {
        result = 2;
    }else if (string === "Wednesday") {
        result = 3;
    }else if (string === "Thursday") {
        result = 4;
    }else if (string === "Friday") {
        result = 5;
    }else if (string === "Saturday") {
        result = 6;
    }else if (string === "Sunday") {
        result = 7;
    }else {
        result = 'error';
    }
    console.log(result)
}
solve('Tuesda')