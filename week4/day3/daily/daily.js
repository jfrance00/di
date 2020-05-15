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
  table.style.width  = '80%';
  table.style.border = '1px solid black';
  document.body.appendChild(table);
  let tbody = document.createElement("tbody");
  table.appendChild(tbody);
  for(i = 0; i < 3; i++){               // create row
    let k = 0
    let tr = table.insertRow("tr");
    for(j = 0; j < 2; j++){
      let td = document.createElement("td");  // create column
      // td_text = document.createTextNode(arr[j].title)
      // td.appendChild(td_text);
      tr.appendChild(td);
      }
  }
  fill_table(tbody);
}

// function fill_table(row)

function fill_table(tbody){   // fills in all of the data
  let td = document.getElementsByTagName("td");
  let row = document.getElementsByTagName("tr");
  for(let i = 0; i < 3; i++){
    let t = 0
    let a = 0;
    let pic = 0
    for(let j = 0;i == 0 && j < 2; j++){
      let td_text = document.createTextNode(allBooks[j].title);
      td[t].appendChild(td_text);
      row[i].appendChild(td[t]);
      t++;
    }
    for(let j = 0; i == 1 && j < 2; j++){
      let td_text = document.createTextNode("Written by " + allBooks[j].author);
      td[a].appendChild(td_text);
      row[i].appendChild(td[a]);
      a++;
    }

  }
}


create_table();
// fill_table(allBooks);


// add table rows with loop the size of the array for(x in allbooks) (minus one lenf)
// enter the information in second loop to each rows
  //challenge will be to add "written by" in second
