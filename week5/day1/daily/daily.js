// Add as many events listeners to one element on your webpage.
// Each listener does a different thing, for instance- change position x,
// change position y, change color, change the font size… and more

document.getElementsByTagName("button")[0].setAttribute('id', 'button');
let btn = document.getElementById("button");
btn.style.display = "grid";
let button_centered = false;


btn.addEventListener("mouseover", function(){     //mouse over change colors
  btn.style.color = "blue";
  btn.style.backgroundColor = "white"
})

btn.addEventListener("mouseout", function(){        //mouse out invert colors
  btn.style.backgroundColor = "blue";
  btn.style.color = "white"
})

function move_button(){                // moves button to center and back on clicks
  if (button_centered === false){
    btn.style.margin = "auto";
    button_centered = true;
    console.log("button centered: " + button_centered)
  } else if (button_centered === true){
    btn.style.marginLeft = "20px";
    button_centered = false;
    console.log("button centered: " + button_centered);
  }
}
