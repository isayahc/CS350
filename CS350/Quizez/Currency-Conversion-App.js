/*
1.Promp user for for value
2. Calculation
3.Console.log

*/

//let dollars = prompt("Enter amount in US Dollars:");
const dollars = process.argv[2];
let pounds = (Number(dollars)*.76);
let euros = (Number(dollars)*.88)

console.log(`${dollars} US Dollars in British Pounds: ${pounds}`);
console.log(`${dollars} US Dollars in Euros: ${euros}`)