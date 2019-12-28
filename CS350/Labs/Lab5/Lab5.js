function sequence(N) 
{ return Array(N).fill().map((_, idx) => idx+1) };

function each(A, func) 
{ for (var i = 0; i < A.length; i++) { A[i] = func(A[i]); } return A; } 

const square = (n) => {return n*n};
const cube = (n) => {return n**3};
const perfectsquares  = (n) => { return /*sequence(n).map(square)*/ each(sequence(n), n => square(n))};
const perfectcubes = (n) => { return /*sequence(10).map(cube)*/each(sequence(n), n => cube(n))};
function perfectpowers (n,p){

   return each(sequence(n), n => Math.pow(n,p));
}

//console.log(cube(2));
console.log(perfectpowers(4,3));
console.log(perfectsquares(3));
console.log(perfectcubes(4));