// Single line object literal
let otherPerson = { name: 'Pesho', age: 20, isMale: true };

// Multi line object literal
let person = {
    name: 'Pesho',
    age: 20,
    isMale: true,
};

// Empty object literal
let emptyObject = {};

// Dynamic assing of properties 
let cat = {};

let propName = 'age';

cat.name = 'Navcho'; // Dot notation
cat['breed'] = 'Persian'; // Bracket notation
cat['fur-color'] = 'yellow';
cat[propName] = 7;

// Object property access
console.log(cat.age);
console.log(cat['fur-color']);
console.log(cat[propName]);

// Object Destructuring Assingment Syntax
let { age, breed, ...rest } = cat;
age = 8;

// First way to Clone object 
let {...clonedCat} = cat;

// Object references
let otherCat = cat; // copy by reference
otherCat.name = 'Garry';

console.log(otherCat.name);
console.log(cat.name);

//Comparing objects
let person1 = {name: 'Pesho'};
let person2 = {name: 'Pesho'};
console.log(person == person2); // Different references
console.log(otherCat == cat); // same references