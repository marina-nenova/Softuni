function solve(speed, area) {
    let currentSpeed = Number(speed);
    let speedLimit = 0;
    switch (area) {
        case 'motorway':
            speedLimit = 130;
            break;
        case 'interstate':
            speedLimit = 90;
            break;
        case 'city':
            speedLimit = 50;
            break;
        case 'residential':
            speedLimit = 20;
            break;
    }
    if (currentSpeed <= speedLimit) {
        console.log(`Driving ${currentSpeed} km/h in a ${speedLimit} zone`);
    } else {
        let status;
        let difference = currentSpeed - speedLimit;
        if (difference >= 40) {
            status = 'reckless driving'
        } else if (difference >=20) {
            status = 'excessive speeding'
        } else {
            status = 'speeding'
        }
        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`);
    }
}

solve(40, 'city')
solve(21, 'residential')
solve(120, 'interstate')
solve(200, 'motorway')