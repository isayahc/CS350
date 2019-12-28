/*


*/
//input: string and n 
//output: the chars in the string are shifted n times
function encrypt(str, N) {

    //blank string
    let result = '';
 
    //an array of the alphabet
    let Plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toLowerCase().split('');


 //from string[0:n]
 /*


 */
    for (let i = 0; i < str.length; i ++) {
       index = Plain.indexOf(str.toLowerCase()[i]);
       result += Plain[(index+N)%26];
     }
 
    return result;

 
 }

 //command inputs
 const str = process.argv[2];
 const N = Number(process.argv[3]);

 console.log(encrypt(str, N));