def min_max():
    dic1 = {
        0 : 10,
        1 : 20,
    }

    dic1[2] = 30
    max_value = max(dic1, key=dic1.get)
    min_value = min(dic1, key=dic1.get)
    print("max value: {} min value: {}".format(max_value, min_value))


def print_products():
    products = {
        'SMART WATCH': 550,
        'PHONE' : 1000,
        'PLAYSTATION': 500,
        'LAPTOP' : 1550,
        'MUSIC PLAYER' : 600,
        'TABLET' : 400
    }
    # in for loop
    for item, price in products.items():
        print('key: {}, value {}'.format(item,price))

    # in while loop - need to figure it out
    # i = 0
    # while i < enumerate(products):
    #     print("enumerate works")
    #     i += 1

#checking if given value is duplicate and remove
def check_remove_duplicates():
    dict = {
        1 : 2,
        2 : 2,
        3 : 3,
    }
    values = dict.values()
    for item in enumerate(dict):
        print("values: ", values)
        # if item[1] == value[item[0]]
        print("Item: ", item)
        print("index: ", item[0])

check_remove_duplicates()






# *********  ignore    *********************************

# in class
# two lists, you need to use python to merge them to a dictionary
list1 =["Rick", "Donald", "Mickey", "Mario"]
list2 = ["Sanchez", "Duck", "Mouse", "Kart"]
result = { }
for i, first_name in enumerate(list1):
    result[first_name] = list2[i]


# Exercise 3 get a number from user and spell number in words

numbers = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
}

# user_input = input("Enter a number")
# for digit in user_input:
#     int(digit)
#     print(numbers[user_input] + " ")



dic1={1:10, 2:20}
dic2={3:30, 4:20}
dic3={5:50, 6:60}



dic4 = {}
# basic code
# for key, value in dic1.items():
#     dic4[key] = value
#
# for key, value in dic2.items():
#     dic4[key] = value
#
# for key, value in dic3.items():
#     dic4[key] = value
#
# # refined
# for dictionary in [dic1, dic2, dic3]
#     for key, value in dictionary.items():
#         dic4[key] = value

# Ask the user to type in his/her favorite fruits.
# What’s the best way to deal with multiple favorites?
# We’ll do it differently here – get input in one string, and ask the user to separate between fruits with a single space, eg. “apple mango cherry”. We will also accept a single fruit as the input here.
# Store the favorite fruit(s) in a list. (How can we ‘convert’ a string of words into a list of words?)
# Now that we have a list of fruits, ask the user to type in the name of any fruit.
# If the user inputs the name of a fruit that is one of his favorites, print, “You chose one of your favorite fruits! Enjoy!”
# If the user inputs the name of a fruit that is not one of his favorites, print, “You chose a new fruit. I hope you enjoy it too!”
# (Bonus: add the word “and” before the last fruit in the list – but only if there are more than 1 favorites!)

# fav_fruits = input("What are your favorite fruits? (separated by space ")
# #best way to deal with multiple favorits is fav_fruits.split(" ")
# fav_fruits_list = fav_fruits.split(" ")
#
# random_fruit = input("Name a fruit")
#
# if random_fruit in fav_fruits_list:
#     print("You chose one of you favorite fruits! Enjoy")
# else:
#     print('You chose a new fruit. I hope you enjoy it too!')


