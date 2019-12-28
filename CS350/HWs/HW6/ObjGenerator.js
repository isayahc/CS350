function getNameNumberGenerator(){
    return {
        counter: 0,
        next: function(){
            return this.counter = (this.counter === 0) ? 15 : this.counter*2
        }
    }
}
var generator = getNameNumberGenerator()
console.log(generator.next())
console.log(generator.next())
console.log(generator.next())