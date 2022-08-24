let names = ['Pesho', 'Gosho', 'Mariyka'];

console.log(names.length);

names.length = 4;
names[4] = 'Stamat'; // Length = 5
names[names.length] = 'Lili'; // (6) ['Pesho', 'Gosho', 'Mariyka', …, 'Stamat', 'Lili']

console.log(names.length);
console.log(names);
console.log(names[names.length - 1]); // last item

// Dirty hack
names['hidden'] = 'Hacker';
console.log(names.hidden);
console.log(names.length);

// Array Destructuring Assignment Syntax and rest operator
let [firstName, secondName, thirdName, _, ...others] = names; // ['Pesho', 'Gosho', 'Mariyka', undefined, 'Stamat', 'Lili'];

console.log(others);