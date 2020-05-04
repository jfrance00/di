

 let fruit = ["Banana", "Apples", "Oranges", "Blueberries"];
 fruit.splice(0,1)
 fruit = fruit.sort()
 fruit.push('Kiwi')
 fruit.splice(0,1)
 fruit.reverse()
 alert(fruit)

 var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
 alert(array2[1][1])
