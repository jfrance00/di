function playTheGame(){
  if (confirm() == true) {  //works
    myNumber = get_number(); //works
    if (isNaN(myNumber)){    //works
      alert("Sorry not a number, Goodbye");  //works
    } else if (myNumber < 0 || myNumber > 10) {    //works
      alert("Sorry, it's not an accepted number, goodbye")  //works
    } else {
      computerNumber = generate_num();
      test(myNumber, computerNumber);     //works
    }
  } else {
    alert("No problem, Goodbye");    //works
  }
}


function test(user_number, computerNumber){
  console.log(computerNumber);
  for(i = 0; i < 3; i++){
    if (i < 3){
      console.log("comp num: " + computerNumber);
      console.log("user num: " + user_number);
      if (check_number(user_number, computerNumber) === true){
        alert("Congrats! You won!");
        return;
      } else if (user_number > computerNumber){
        alert("Your number is too big. Guess again");
        user_number = get_number();
        check_number(user_number, computerNumber);
      } else if (user_number < computerNumber){
        alert("Your number is too small. Guess again")
        user_number = get_number();
        check_number(user_number, computerNumber);
      }
    } else {
    alert("Good try, but needed to guess " + computerNumber);
    }
  }
}

function confirm(){   //works
  let user_play = prompt("Do you want to play the game?");
  return (user_play === "yes" || user_play === "Yes" || user_play === "y" || user_play === "Y");
}

function get_number(){ //works
  myNumber = Number(prompt("Enter a number between 1 and 10: "));
  return myNumber
}

function generate_num(){
    computerNumber = (Math.floor(Math.random()*10));
    return computerNumber;
}

function check_number(user_number, comp_num){
  if (user_number === comp_num){
    return true;
  } else {
    return false;
  }
}

// Create a function named test that takes 2 parameters : myNumber and computerNumber, inside this function create a few conditions
// If myNumber is bigger than the computerNumber, alert the user that it's bigger and he has to guess again
// If myNumber is lower than the computerNumber, alert the user that it's lower and he has to guess again
// If the user guessed more than 3 times, alert him that he can't try again and give him the number that the computer had in mind
