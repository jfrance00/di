let operators = ["+", "-", "*", "/"]
let numbers = ['0','1','2','3','4','5','6','7','8','9','.'] //should be able to get #s from DOM
let num = [];

function my_f(input){
   if (input == "="){
    calculate();
    } else {
    display();
    num.push(input);
    return num;
  }
}

function calculate(){
  solution = eval(num.join(""));
  console.log(solution);
  reset();
}

function reset(){
  length = num.length;
  num.splice(0,length);
  return num;
}

function clear(){   //removes last number
  num.pop();
  console.log(num);
  return num;
}

function display(){
  let display = getElementById("user_number");
  displayNum = num.join("");
  display.value = displayNum;
}
