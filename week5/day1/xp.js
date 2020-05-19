// Exercise 1
// Fade out the 2nd paragraph over 2000 milliseconds, when it’s clicked
// Get the value in the inputs and append it to the end of the html, inside a table
// h1 = document.querySelector('tagName');
let h1 = document.querySelector("h1");
let para = document.querySelectorAll("p")
h1.addEventListener("click", function remove_h1_onclick(){
    h1.remove();
})

para[0].addEventListener("click", function() {
  para[0].hidden = true;
});

function new_tag(){
  for (i = 0; i < para.length; i++) {
      para[i].className += 'para_article';
  }
}

function remove_para(){    //should remove the last paragrapgh element
  let para = document.querySelectorAll("p");
   para[para.length - 1].remove();
 }

function resize_h1(){
  let font_size = Math.floor(Math.random() * (100 - 1)) + 1;
  h1.style.fontSize = font_size +"px";
}


new_tag();
remove_para();
resize_h1();

//Exercise 2




// Exercise 3
