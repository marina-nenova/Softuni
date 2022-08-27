let phoneBook = {
    'Ivan Petrov': '12321231',
    'Georgi Georgiev': '2139804712',
    'Peter Petrov': '123123123',
};

// Accessing and assigning
phoneBook['Ivan Petrov'] = '897897987'
console.log(phoneBook['Ivan Petrov']);

// Iteration - for in
for (key in phoneBook) {
    console.log(`${key} - ${phoneBook[key]}`);
}

// Iteration - methods
let names = Object.keys(phoneBook);
let phones = Object.values(phoneBook);
console.log(names);
console.log(phones);

Object.keys(phoneBook).forEach(x => {
    console.log(`${x} - ${phoneBook[x]}`);
});

// Used for sorting of object
let entries = Object.entries(phoneBook);

for (const kvp of entries) {
    console.log(kvp);
}