

function powerz (x,n){
    for(let i=0; i <=x; i++){
        console.log(`${n}^${i}=${n**i}`);
    }
}

//based on x^n
const x = process.argv[2];
const n = process.argv[3];
powerz(x,n);
