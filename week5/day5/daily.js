// Part 1
function pyramid1(){         //for more advanced try printing to page
let stars = "* "            //sets intitial variable
for(let i = 0; i < 5; i++){
console.log(stars);
  stars = stars.concat("* ");     //indexes variable
  }
}
pyramid1();

// Part 2

function pyramid2(){
  console.log(" ");
  let rows = 5
  let space = "  ";
  let stars = "* ";
  for(let i = 1; i <= rows; i++){
    let str = "";                                   // each row starts with clean string
    for(let spaces = 1; spaces <= rows-i; spaces++){    //spaces
      str = str+space;
    }
    for(let col = 1; col <= 1; col++){              //places stars
      str = str+stars;
      console.log(str);
      stars+="* * ";
    }
  }
} //close function



pyramid2();
