/*
Create a function called product  
with default argument values that 
takes up to 10 parameters. The function 
returns the product of its arguments

*/

const product = function (...nums){
    if(nums.length >10){
        console.error("too many arguments");
        Process.exit(1);
    }
    let result = 1;
    for(let i=0; i< nums.length; i++){
        result*=nums[i];
    }
    return result;

}

console.log(product(1,2,3));
console.log(product(3,4));
console.log(product(6));
console.log(product(1,2,3,5,10));
console.log(product(1,2,3,4,5,6,7,8,9,10));