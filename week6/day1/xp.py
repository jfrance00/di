# exercise 1

hello = "hello world"
print(hello*4)

# exercise 2
print((99^3)*8)

# exercise 3
name = "Julie"
age = 30
shoe_size = 39
age = str(age)
shoe_size = str(shoe_size)
info = "It is hard to make and interesting sentance with " + name + ", my age " + str(age) + ", and my shoe size" + shoe_size
print(info)

# exercise 4
computer_brand = "Dell"
print("I have a", computer_brand)

# exercise 5
5 < 3 #false
3 == 3 #true
3 == "3" #false
#"3" > 3 #false - just kidding, you can't do that
"Hello" == "hello" #false

# exercise 6
user_height = int(input("How tall are you?"))
if(user_height > 35):
    print("You can ride the rollercoaster")
else:
    print("You are not tall enough to ride")

# exercise 7
number = int(input("Enter a number "))
if (number % 2 == 0):
    print("number is even")
else:
    print("number is odd")
