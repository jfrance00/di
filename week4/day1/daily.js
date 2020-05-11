let stars = "*********";
let hello = "* Hello *";
let world = "* World *";
let inside = "* in    *";
let a = "* a     *";
let frame = "* frame *";

let print_arr = [stars, hello, world, inside, a, frame, stars];

function print(arr){
  for(let x of arr){
    console.log(x);
  }
}
