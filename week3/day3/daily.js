// Create a string that has the word “not” and “bad” inside
// Create another variable that should find the first appearance of the substring ‘not’ and ‘bad’.
// If the ‘bad’ follows the ‘not’, then it should replace the whole ‘not’…’bad’ substring with ‘good’ than console.log the result.
// If it doesn’t find ‘not’ and ‘bad’ in the right sequence (or at all), just console.log the original sentence.

let str = "You're not so bad after all";
let key = "bad"
let index_bad = str.indexOf("bad");
let index_not = str.indexOf("not");
let switch_length = str.indexOf("bad") + key.length - str.indexOf("not");

if(index_not < index_bad) {
  let newString = str.replace("not so bad", "good");
  console.log(newString);
} else {
  console.log(str);
}
