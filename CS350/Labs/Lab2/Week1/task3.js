/* 
1.Copy Program
2.run from command line n
3.

***n is input as a string not a number.
*/
function add2(n) {
    let two = 2;
    return two + n; }
  const inputN = Number(process.argv[2]);
  const result = add2(inputN);
  console.log(result);