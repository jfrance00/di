let family = { //exercise 1
  numMembers : 4,
  mom : 'Janet',
  dad : 'John',
  kid1 : 'Jimmy',
  kid2 : 'Jessica'
}
for(let x in family) {
  console.log(x);
}
for(let x in family) {
  console.log(family[x]);
}


// If it is than inform the owner that he has to inscrease the rent of Dan. And
//change the rent of Dan accordingly inside the object.

var building = {            //exercise 2
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10],
    },
}

console.log(building.number_levels);               //number of number_levels
console.log(building.number_of_apt_by_level[1]);   // display certain # apts and add them
console.log(building.number_of_apt_by_level[3]);
console.log(building.number_of_apt_by_level[1] + building.number_of_apt_by_level[3]);

console.log(building.name_of_tenants[1] +" "+ building.number_of_rooms_and_rent['Dan']);// second tenenat # of rooms

let sumRent = building.number_of_rooms_and_rent['Sarah'][1] + building.number_of_rooms_and_rent['Dan'][1] > building.number_of_rooms_and_rent['David'][1]//check Sarah rent + David rent > Dan rent
console.log(sumRent);             //returns if sum of sarah and david rent is bigger than dan sumRent

if(sumRent) {
  console.log("You should increase Dan's rent");
}

building.number_of_rooms_and_rent['David'][1] = 600 // raises David's rent

// create two people objects, compare BMIs
  let person1 = {        // exercise 3
    "name" : "Tim",
    "mass" : 70,
    "height" : 1.65
  };
  let person2 = {
    "name" : "Jim",
    "mass" : 90,
    "height" : 1.95
  }
 let bmi_person1 = person1.mass/(person1.height * person1.height)
 let bmi_person2 = person2.mass/(person2.height * person2.height)
 if(bmi_person1 > bmi_person2){
   console.log(person1.name);
 } else {
   console.log(person2.name);
 }
