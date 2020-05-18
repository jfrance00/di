// Create an array called allBooks. This array contain objects. Each object is
//a book that has 4 keys : title, author,image(a url) and alreadyRead which is a boolean.

// Initiate the array with 2 books of your choice.
// Requirements:
// On the page you have to render the books inside a table.
// For each book :
// You have to display the book’s title then “written by” and then the book’s
//author (Ex: HarryPotter written by JKRolling)

// The width of the image has to be set to 100.
// If the book is already read. Set the color of the book details to red

let allBooks = [
  {
    title : "Alice in Wonderland",
    author : "Lewis Carrol",
    image : "https://images-na.ssl-images-amazon.com/images/I/61KnsVaz3hL._SX412_BO1,204,203,200_.jpg",
    alreadyRead : true
  },
  {
    title : "War and Peace",
    author : "Leo Tolstoy",
    image : "https://images-na.ssl-images-amazon.com/images/I/51J1nb00FLL._SX330_BO1,204,203,200_.jpg",
    alreadyRead : false
  }
];

function create_table(){         //creates table
  let table = document.createElement("table");
  let tbody = document.createElement("tbody");
  table.style.width  = '80%';
  table.style.border = '1px solid black';
  document.body.appendChild(table);
  table.appendChild(tbody);
  fill_table(tbody);
}


function fill_table(tbody){   // fills in all of the data
  for(let i = 0; i < allBooks.length; i++){
    let tbody = document.getElementsByTagName("tbody")[0];
    let tr = tbody.insertRow();
    tr.classList.add(`row_${i}`)
    for(let j = 0; j < Object.keys(allBooks[i]).length - 1; j++){
        let td = document.createElement("td");
        if (j == 0){
        let td_text = document.createTextNode(allBooks[i].title)    //prints the title in the row
        td.appendChild(td_text);
      } else if (j == 1){
        let td_text = document.createTextNode("written by " + allBooks[i].author)    //prints the author in the row
        td.appendChild(td_text);
      } else if (j == 2){
        let td_text = document.createTextNode(allBooks[i].image)   //prints the image in the row
        td.appendChild(td_text);
      }
      // if_read_color(allBooks[i])
      tr.appendChild(td);
      }
    tbody.appendChild(tr);
  }
}

// function if_read_color(book){
//   for (let i = 0; i < allBooks.length; i++){
//     let tr = document.getElementById("row_1");
//     if(book.alreadyRead == true){
//       tr.style.color = "red";
//     } else {
//       tr.style.color = "black";
//     }
//   }
// }

create_table();
