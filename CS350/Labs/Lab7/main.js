var cart=[   {"name":"Biscuits", "type":"regular", "category":"food", "price": 2.0},   
{"name":"Monitor", "type":"prime", "category":"tech", "price": 120},   
{"name":"Mouse", "type":"prime", "category":"tech", "price": 25},   
{"name":"dress", "type":"regular", "category":"clothes", "price": 50},   
{"name":"XL Monitor", "type":"prime", "category":"tech", "price": 160},   
{"name":"Cookies", "type":"regular", "category":"food", "price": 16}, ] 

console.log(cart);

function isPrime (item){
    return (item.type === "prime");
}

let isNotPrime = item => !isPrime(item); 

const applyShippingCost = (item) => {
    isPrime(item) ? item.price : (item.price + 5); 
    return item;
}

let applyCoupon = (item) => {
    (item.category === 'tech') ? (item.price) : (item.price/5)                    
    return item; 
}

let applySalesTax = (item) => {     
    const SALES_TAX = 6.00;     
    item.price += (item.price / 100 * SALES_TAX);     
    return item; 
};


function totalCost(cart){   
    return cart.reduce((accumulator, item) => {       
        accumulator += item.price;       
        return accumulator;   
    }, 0); 
}

console.log(cart);
let primeDiscount = totalCost(cart.filter(isPrime).map(applyCoupon).map(applySalesTax));

let NonPrimecost = totalCost(cart.filter(isNotPrime).map(applyCoupon).map(applyShippingCost).map(applySalesTax));

let AllItem = totalCost(cart.map(applyShippingCost).map(applySalesTax));


//console.log(cart);
console.log("space");
//console.log(primeDiscount);
console.log("space");
//console.log(NonPrimecost);
console.log("space");
//console.log(AllItem);
console.log("space");

//console.log(cart.map(applyShippingCost));
console.log(cart);
