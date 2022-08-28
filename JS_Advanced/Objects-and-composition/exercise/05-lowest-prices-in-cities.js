function solve(array) {
    let products = [];

    for (const line of array) {
        let [town, product, price] = line.split(' | ');
        price = Number(price);

        if (products.filter(x => x.product === product).length > 0) {

            let obj = products.find(x => x.product === product);

            if (obj.price > price) {
                obj.price = price;
                obj.town = town;
            }
        } else {
            let obj = {product, town, price};
            products.push(obj);
        }
    }
    for (const prod of products) {
        console.log(`${prod.product} -> ${prod.price} (${prod.town})`);
    }
}

solve(['Sample Town | Sample Product | 1000',
    'Sample Town | Orange | 2',
    'Sample Town | Peach | 1',
    'Sofia | Orange | 3',
    'Sofia | Peach | 2',
    'New York | Sample Product | 1000.1',
    'New York | Burger | 10']
)