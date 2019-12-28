let people = [   
    {name: "Amy", pounds_weight: 152, inches_height: 63},   
    {name: "Joe", pounds_weight: 120, inches_height: 64},   
    {name: "Tom", pounds_weight: 210, inches_height: 78},   
    {name: "Jim", pounds_weight: 180, inches_height: 68},   
    {name: "Jen", pounds_weight: 120, inches_height: 62},   
    {name: "Ann", pounds_weight: 252, inches_height: 63},   
    {name: "Ben", pounds_weight: 240, inches_height: 72},
];

//Task #1 & #2 & #3

const poundstokg = x => x * 0.45359237;
const inchestometers = x => x * 0.0254;

function addbmi(Person){
    bmi = poundstokg(Person.pounds_weight)/(inchestometers(Person.inches_height))**2;
    Person.bmi = bmi;
    return Person;
}
let isOverweight = Person => (Person.bmi > 25.0 && Person.bmi <30);
let isObese = Person => (Person.bmi > 30);

let OverWeightPeople = people.map(addbmi).filter(isOverweight);
let Obese_people = people.map(addbmi).filter(isObese);

