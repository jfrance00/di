// Sort the following array in descending order using for loops (Not using built in sort methods).
// const arr = [5,0,9,1,7,4,2,6,3,8];
// The output should be: [9,8,7,6,5,4,3,2,1,0]
// Hint: The algorithm is called “Bubble Sort”
//
// Use a temporary variable to swap values in the array.
//
// Use 2 “nested” for loops (Nested means one inside the other).
//
// Using the “.toString()” method, convert the array to a string.
//
// Using the “.join()”, convert the array to a string. Try passing different values into the join.
// Eg .join(“+”), .join(” “), .join(“”)

const arr = [5,0,9,1,7,4,2,6,3,8];
// sort array
for(let number of arr){
  for(let i = 0; i < arr.length; i++){
    if (arr[i] > arr[i+1]){
      let temp = arr[i];
      arr[i] = arr[i+1];
      arr[i+1] = temp;
    }
  }
}
console.log(arr);

arr.toString();
arr.join(" ");
arr.join(',');
arr.join('+');
