function solve(steps, footPrint, speedKmH) {
    let distanceInMeters = steps * footPrint;
    let speed = speedKmH * 1000 / 3600;
    let rest = Math.floor(distanceInMeters / 500) * 60;
    let timeInSeconds = (distanceInMeters / speed) + rest;

    let hours = Math.floor(timeInSeconds / 3600)
    let minutes = Math.floor(timeInSeconds / 60)
    let seconds = timeInSeconds % 60
    
    console.log(`${hours.toFixed(0).padStart(2, '0')}:${minutes.toFixed(0).padStart(2, '0')}:${seconds.toFixed(0).padStart(2, '0')}`);
}

solve(2564, 0.70, 5.5)