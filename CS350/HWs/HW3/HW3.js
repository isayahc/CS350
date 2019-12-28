data = [
    {
      name: 'Butters',
      age: 3,
      type: 'dog'
    },
    {
      name: 'Lizzy',
      age: 6,
      type: 'dog'
    },
    {
      name: 'Red',
      age: 1,
      type: 'cat'
    },
    {
      name: 'Joe',
      age: 3,
      type: 'dog'
    },
    {
      name: 'John',
      age: 7,
      type: 'cat'
    },
    {
      name: 'Jona',
      age: 10,
      type: 'dog'
    },
    {
      name: 'Joey',
      age: 5,
      type: 'cat'
    },
    {
      name: 'Jay',
      age: 9,
      type: 'cat'
    },
    {
      name: 'Jason',
      age: 7,
      type: 'dog'
    },
    {
      name: 'Jonana',
      age: 9,
      type: 'cat'
    },
    {
      name: 'Willow',
      age: 2,
      type: 'dog'
    },
    {
      name:"Darthovurt",
      age: 4,
      type: 'cat',
    },
    {

    }
  ];

let isDog = (animal) => {
    return animal.type === 'dog';
  }
let isCat = (animal) => {
  return animal.type === 'cat';
}
let catYears = (animal) => {
  return animal.age  * 10;
}
let dogYears = (animal) => {
    return animal.age * 7;
  }
let sum = (sum, animal) => {
    return sum + animal;
  }
  let Dogages = data
  .filter(isDog)
  .map(dogYears)
  .reduce(sum);

  let Catages = data
  .filter(isCat)
  .map(catYears)
  .reduce(sum);




console.log(`Cat ages : ${Catages}`);
console.log(`Dog ages : ${Dogages}`);