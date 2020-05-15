//exercise 1   make function check driver age
let age = Number(prompt("What is your age"))

function checkDriverAge(age){
    if (age < 18){
    alert("Sorry, you are too yound to drive this car. Powering off");
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

  // exercise 3

var stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

var prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

let shopping_list = ["banana","pear","orange"]

function myBill(){
  let total = 0;
  for(let item of shopping_list){
    if(item in prices){
      total = total + prices[item];
    }
  }
  return total;
}

// Depending on the list of items that you have in your shopping list and the prices listed in the 2nd object, return the total of the expense for your groceries.
// Call the function myBill
// Bonus: In the function above, only add the price if the item is in stock.
// If the item is in stock, decrease the item’s stock by 1
