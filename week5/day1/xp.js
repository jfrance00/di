// // Exercise 1
// Get the value in the inputs and append it to the end of the html, inside a table
let h1 = document.querySelector("h1");
let para = document.querySelectorAll("p")
para[1].setAttribute("id", "fadeout");          //id for jquery fadeout
let input = document.getElementsByTagName("input");

h1.addEventListener("click", function remove_h1_onclick(){  //removes h1 onclick
    h1.remove();
})

para[1].addEventListener("click", function(){
  let op = 1;
  setInterval(function () {
        if (op >= 0.0){
        para[1].style.opacity = op;
        op -= 0.1;
      }
    }, 2000);
})

function new_tag(){                        //creates tag "para" for <p>
  for (i = 0; i < para.length; i++) {
      para[i].className += 'para_article';
  }
}

para[0].addEventListener("click", function() {        // eventListener to hide 1st para on click
  para[0].hidden = true;
});



function remove_para(){                          //function to remove the last paragrapgh element
  let para = document.querySelectorAll("p");
   para[para.length - 1].remove();
 }

function resize_h1(){                                       //resize h1
  let font_size = Math.floor(Math.random() * (100 - 1)) + 1;
  h1.style.fontSize = font_size +"px";
}

function collect_user_data(){
  on enter take input

  input_to_table
}

function input_to_table(){
  let table = document.createElement("table");
  document.body.appendChild(table);
  let tr = table.insertRow();
  for(let x in input){
    let td = document.createElement("td");
    let text = document.createTextNode(input[x])
    td.appendChild(document.createTextNode());
    tr.appendChild(td)
  }
}




new_tag();                    //call relevant functions
remove_para();
resize_h1();

//Exercise 2

function getBold_items(){
  let bold = document.getElementsByTagName("strong")
  return bold;
}


function highlight(){
  let bold = getBold_items()
  for(let i of bold){
    i.style.color = "blue";
    }
  }

  function return_normal(){
    let bold = getBold_items()
    for(let i of bold){
      i.style.color = "black";
      }
    }

  let boldItems = getBold_items();
  for(let x of boldItems){
    x.addEventListener("mouseover", highlight);
  }
  for(let x of boldItems){
    x.addEventListener("mouseout", return_normal);
  }


// Exercise 3
