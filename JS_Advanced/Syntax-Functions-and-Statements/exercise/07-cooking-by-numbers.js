function solve(n, p1, p2, p3, p4, p5) {
    let number = Number(n);
    let arrOfCommands = [p1, p2, p3, p4, p5]

    let chop = function() {
        return number / 2;
    };
    let dice = function() {
        return Math.sqrt(number);
    };
    let spice = function() {
        return number + 1;
    };
    let bake = function() {
        return number * 3;
    };
    let fillet = function() {
        return number * 0.80;
    };
    for (let i = 0; i < arrOfCommands.length; i++) {
        const command = arrOfCommands[i];
        switch (command) {
            case 'chop':
                number = chop();
                break;
            case 'dice':
                number = dice();
                break;
            case 'spice':
                number = spice();
                break;
            case 'bake':
                number = bake();
                break;
            case 'fillet':
                number = fillet();
                break;
        }   console.log(number);
    }
}

solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet')