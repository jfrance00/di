let operators = ["+", "-", "*", "/"]
let numbers = ['0','1','2','3','4','5','6','7','8','9','.'] //should be able to get #s from DOM
let num = [];

function my_f(input){
  let calc = document.getElementsByClassName("number")
  let operator = document.getElementsByClassName("operator")
  if (numbers.includes(input)){
    console.log(input + " number in loop");
    num.push(input);
    return num;
  } else if (operators.includes(input)){
    console.log("operator");
    num.push(input);
    return num;
  } else if (input == "="){
    calculate();
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
