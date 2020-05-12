//exercise 1   make function check driver age
var age = prompt(“What is your age?”);


function checkDriverAge(age){
    if (age < 18){
    alert("Sorry, you are too yound to drive this car. Powering offe");
    } else if (age > 18) {
    alert("Powering On. Enjoy the ride!");
    } else if (age === 18){
    alert("Congratulations on your first year of driving. Enjoy the ride!");
    }
    return
}

//exercise 2
amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function item_to_check() {
  let item = prompt("What item do you want to check? ");
  return item;
}
  let user_item = item_to_check();

function check_basket(item){
  if (item in amazonBasket){
      return true;
    } else {
      return false;
    }
  }
