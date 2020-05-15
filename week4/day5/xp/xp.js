console.log("it is connected");


let operators = ["+", "-", "x", "/"]
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
    convert_int(num);        //user done input of first number, converts array to int
    clear_input();              // clears array num for future inputs
    action = input;
    return action;
  } else if (input == "="){
    calculate();
  }
}

function convert_int(num){
  num1 = Number(num.join(""));
  return num1;
}

function calculate(){
  num2 = Number(num.join(""));  //should find a way to make variable names dynamic so can have one function for this
  if (action == "+"){           // if addition
    result = num1 + num2;
    return result
  } else if (action == "-") {     //subtraction
    result = num1 - num2;
    return result;
  } else if (action == "x"){    //multiplication
    result = num1 * num2;
    return result;
  } else if (action == "/"){  //division
    result = num1 / num2;
    return result;
  }
}

function reset(){
  num1 = 0
  num2 = 0
}

function clear(){   //removes last number
  num.pop();
  console.log(num);
  return num;
}

function clear_input(){
  num = [];
  return num;
}
