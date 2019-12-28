function getNameNumberGenerator(){
    var counter = 0;
    return function (){
        return counter===0 ? counter+=15 : counter+=counter;
    }
}


var generator = getNameNumberGenerator();
var generator2 = getNameNumberGenerator()
console.log(generator());
console.log(generator());
console.log(generator());
console.log(generator());