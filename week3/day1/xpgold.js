let me = ['my', 'favorite', 'color', 'is', 'blue'];
me.join(' ')


//two variables, swap out first two characters, concatonate

let str1 = "dog";
let str2 = "cat"

let swap_start_str1 = str1.substr(0,2)
let swap_start_str2 = str2.substr(0,2)
let swap_last_str1 = str1.substr(2)
let swap_last_str2 = str2.substr(2)

let new_string = swap_start_str2 + swap_last_str1 +' '+ swap_start_str1 + swap_last_str2


// desired output cag dot
