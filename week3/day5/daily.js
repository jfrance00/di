// Ask the user for several words and save them. Check if the words given are strings
// Determine which word has the greatest number of repeated letters and console.log this word.

let words = prompt("Please enter some words:")   //collect words
arr_words = words.split(" ")    //break words into array

for(let i = 0; i < arr_words.length; i++){
  if (typeof arr_words[i] == "string"){    //check if string
    console.log("all words are strings");
  }
}



  let word_index = 0
  for(let x of arr_words){
    let single_word = x.split("");
    let repeat_char = 0;
    for(let i = 0; i < single_word.length; i++){
      if (single_word.indexOf(single_word[i]) !== single_word.lastIndexOf(single_word[i])){
        repeat_char++;
      }
    }
    if (repeat_char >= 1){
      console.log(x);
    }
  }
