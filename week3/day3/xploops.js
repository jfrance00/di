let colors = ['purple','blue','green'];
let i = 1
for(let x of colors){
    console.log("my #" +i+ " favorite color is " +x)
    i++
}


function number() {
  let userNum = Number(prompt("please enter a number")) //initial input
  while(userNum < 10) {
    userNum = Number(prompt("please enter a number")) //continue to ask input if num < 10
    }
  }





  // Write a variable last which value is the last element of the array
  // Hint: What is the relationship between the index of the last element in the array and the length of the array?


  var people = ["Greg", "Mary", "Devon", "James"];
  for(let x of people) {
    console.log(x);
  }
  people.shift();
  people.splice(2,1,"Jason")     // change "James" for "Jason"
  people.push("Julie")           //add Julie
  // array is now (4) ["Mary", "Devon", "Jason", "Julie"]
  for(let x of people) {         //console.log array except for Mary
    if (x == "Mary"){
      break;
    }
    console.log(x)
  }

  let newPeople = people.slice(1,3); //copy w/o "Mary" or my name
  people.indexOf("Mary") //command to give index of Mary
  people.indexOf("foo") //index of "foo"

  let newVar = people[people.length - 1] //new variable that is the last element of array

  // 2. console.log just the even numbers
  // 3. Bonus: Return the largest number of the array
  var age = [20,5,12,43,98,55];
  let total = 0
  for(let x of age) { //loop to sun all the elements
    total = total + x;
  }
  console.log(total)

  for(let x of age) { //loop to return even numbers
    if (x % 2 == 0) {
      console.log(x);
    }
  }

  let biggerNum = age[0]  //bigger number loop
  for(let i = 0; i < age.length; i++){
    if(age[i] > biggerNum){
      biggerNum = age[i];
    }
  }
  console.log(biggerNum)
