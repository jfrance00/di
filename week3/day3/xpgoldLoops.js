
let userNum = Number(prompt("Enter a number")); // exercise 1

if(userNum % 2 == 0){
  console.log(userNum + " is an even number");
} else {
  console.log(userNum + " is an odd number");
}

let x = 6; //exercise 2
let y = 3;
if (x > y){
  console.log(x);
} else {
  console.log(y);
}


let language = prompt("Which Language do you speak"); //exercise 3
switch(language) {
  case 'French':
    console.log("Bonjour");
    break;
  case 'English':
    console.log("Hello");
    break;
  case 'Hebrew':
    console.log("Shalom");
    break;
  default:
    console.log(':)');
}


let grade = Number(prompt("please enter your grade (in percentage)")); //exercise 4
if (grade > 90){
  console.log('A');
} else if (grade > 80) {
  console.log('B');
} else if (grade > 70) {
  console.log('C');
} else {
  console.log('D');
}
