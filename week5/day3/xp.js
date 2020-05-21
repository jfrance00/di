//exercise 1
let interval;
function myMove(){
  let small_box = document.getElementById("animate");
  let position = 0;                                         //variable for position (at start)
  let interval = setInterval(move_box_right, 10)
  function move_box_right(){
    if (position === 350){                                 // trigger clearInterval at desired end
      clearInterval(interval)
    } else {                                             //move box as long as clear not triggered
      position++;
      small_box.style.top = position + "px";
      small_box.style.left = position + "px";
      }
    }
  }


function stop_box(stopTime){
  clearInterval(interval)
}

//exercise 2
let box = document.getElementById("drag");

function drag_on_target(e){                    // what happens when object enters target
  e.preventDefault();
  box.style.backgroundColor = "lightblue";      //How can I make the moving object change color?
}

function leave_target(e){                      // return to original state when leaving target
  box.style.backgroundColor = "blue";          // How would I make it possible to drop object outside of target in return
}

function drag(e) {                              //necessary function for dragged objects
  e.dataTransfer.setData("text", e.target.id);
}

function drop(e){                           //transfers data when drop executed
  e.preventDefault();
  let data = e.dataTransfer.getData("text");
  e.target.appendChild(document.getElementById(data));
}
