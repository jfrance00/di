
function get_numbers(){                                 //exercise 1
  var num1 = Number(prompt("Enter a big number"));
  var num2 = Number(prompt("Enter a smaller number"));
}

function check_less_hundred (a,b){
  if (a + b < 100){
    return true;
  } else {
    return false;
  }
}

//___________________________________________________________________________________

function check_remainder(a,b){        //exercise 2
let remainder = a % b;
return remainder;
}

//__________________________________________________________________________________-


function divides_evenly(a,b) {           //exercise 3
  if (a % b == 0){
    return true;
  } else {
    return false
  }
}

//___________________________________________________________________________________

var user_num = Number(prompt("enter a number"));    //exercise 4

var arr = [4,6,2,8,9,10];

function check_array(num){
  var contains = arr.includes(num);
  return contains;
}

check_array(user_num);
