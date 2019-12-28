const inputBox = document.querySelector("#US");
const answerParagraph = document.querySelector("#answer");

inputBox.addEventListener('input', report);

function report() {
  const Dollars = inputBox.value;
  const Pounds = (Dollars * 0.76); 
  
  if (isNaN(Pounds)) {
    answerParagraph.textContent = '?';
  } else {
    answerParagraph.textContent = Pounds;
  }
}