let word = [];
let tracker = [];

function word_input(){
  word_prompt = prompt("Please enter a word");
  word = word_prompt.split('');
  return word;
}

function guess_tracker(){
  tracker = word;
  tracker.splice(0, tracker.length, "*");
}
