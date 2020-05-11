//exercise 1
var age = prompt(“What is your age?”);

if (Number(age) < 18) {
alert(“Sorry, you are too yound to drive this car. Powering off”);
} else if (Number(age) > 18) {
alert(“Powering On. Enjoy the ride!”);
} else if (Number(age) === 18) {
alert(“Congratulations on your first year of driving. Enjoy the ride!”);
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

function check_basket(item){
  for(let x in amazonBasket){
    if(x == item){
      return true;
    }
    //if "return false" written here we will get false if the argument is not the first item in the object
  }
  return false;
}
