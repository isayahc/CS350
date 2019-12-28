const fibnum = 1.618034;

function fib (){
    var n = -1;
    return function (){
        n++;
        return Math.floor((fibnum**n - (1-fibnum)**n)/Math.sqrt(5))
    }
}

function factorial(){
    var counter = 0;
    return function(){
        counter++;
        var total;
        total*=counter;
        return total

        
    }
}

function generator(){
    var counter = 0;
    return function(){
        (counter===0? 1:counter*counter-1)  
        return counter;
    }

}

function evennum(){
    var counter = 0;
    return function (){
        counter = counter +2
        return counter;
    }
}

function oddnum(){
    var counter = -1;
    return function (){
        counter = counter +2
        return counter;
    }
}

function PerfectSquares(){
    var counter = -1;
    return function (){
        counter ++;
        return 2**counter;
    }
}

function Gentest (f,i){
    for(let iter = 0; iter <= i; iter++){
        console.log(f())
    }
}

function factorialize(num){
    return(num);
}


var genfib = fib();
var genns = PerfectSquares();
var gene = evennum();
var fact = factorial();
Gentest(fact(),10);



