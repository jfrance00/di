let numbers1 =  [0, -1, 4]     //exercise 1


                   // exercise 2



let grades = {       //exercise 3
    david:  80,
    vinoth: 77,
    divya: 88,
    ishitha: 95,
    thomas: 68,
    lea: 77
}

// Write a program to check which student has the best grade. Console.log the name of the student.
// Write a program to check which student has the worst grade. Console.log the name of the student.
// Write a program to check if a few students have the same grade. Console.log their names.



function find_biggest_grade(){  //biggest grade
  let biggest_grade = 0;
  for(let x in grades) {
      if (grades[x] > biggest_grade){
        biggest_grade = grades[x]; //if change to biggest_grade = x it returns David and not Ishitha (even though as is it returns 95)
        name_best_grade = x;
      }
  }
  return name_best_grade;

}

function find_smallest_grade(){  //smallest grade
  let smallest_grade = 100;
  for(let x in grades) {
      if (grades[x] < smallest_grade){
        smallest_grade = grades[x];
      }
  }
  return smallest_grade
}

//function get_student_names(search_value){
//  let keys = Object.keys(grades);
//  let values = Object.values(grades);
//  let grade_index = values.findIndex(search_value);
//  let name =
//}
