var cart=[
    {"name":"Biscuits", "type":"regular", "category":"food", "price": 2.0},
    {"name":"Monitor", "type":"prime", "category":"tech", "price": 119.99},
    {"name":"Mouse", "type":"prime", "category":"tech", "price": 25.50},
    {"name":"dress", "type":"regular", "category":"clothes", "price": 49.90},
]

function isPrime(item){
    return item.type === "prime";

}

function primeItems(cart){
  return cart.filter(isPrime);
}

function istech (x) {
    if (x.category === "tech") 
        return true; 
    }
    return false;
      
function applyCoupon(cart){
  // write your code here
  let x =cart.map(istech(cart.category));
  return x;
}
console.log("wtf");

