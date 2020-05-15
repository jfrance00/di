
// exercise 1

let navbar = document.getElementById("navBar");
navbar.setAttribute("id", "socialNetworkNavigation");
let logout = document.createElement("li");
let logout_text = document.createTextNode("Logout");
logout.appendChild(logout_text);
navbar.firstElementChild.appendChild(logout);

let navlist = navbar.firstElementChild // variable for ul

navlist.firstElementChild
navlist.lastElementChild

//exercise 2

// Change each first name of the <ul> by your name
// Add add the end of each <ul>, a paragraph that says “Hey students”
// Delete the <li> Sarah
// Bonus:
// Change the class of <ul> by “student_list”
// Add a class “university” to the first <ul>

let name = document.getElementsByClassName('list')[0];
name.lastElementChild.innerHTML = "Richard";
let first_person = document.getElementsByClassName("list").firstElementChild
