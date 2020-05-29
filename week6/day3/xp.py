#exercise

# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.pop(0)
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# apple_occurances = basket.count("Apples")
# basket = []
#
# print(basket)
# print("apple occurances:", apple_occurances)

# Exercise 1

# my_fav_numbers = {3, 6, 9}
# print(my_fav_numbers)
# my_fav_numbers.update([12, 14])
# print(my_fav_numbers)
# my_fav_numbers.remove(14)
# print(my_fav_numbers)
# friend_fav_numbers = {1, 5, 7}
# our_fav_numbers = set(list(my_fav_numbers) + list(friend_fav_numbers))
# print(our_fav_numbers)

# Exercise 2
my_fav_numbers = (3, 6, 9)
print(my_fav_numbers)
temp_fav = list(my_fav_numbers)
print(temp_fav)
temp_fav.append(12)
temp_fav.append(14)
my_fav_numbers = tuple(temp_fav)
temp_fav.remove(14)
my_fav_numbers = tuple(temp_fav)
print(my_fav_numbers)
friend_favorite_numbers = (1, 5, 7)
our_favorite_numbers = my_fav_numbers + friend_favorite_numbers
print(our_favorite_numbers)

# Exercise 3
# 1. Float = number with a decimal point
# 2. Can create sequence of floats (as list or tuple, not string)
# 3. ?
# 4 loop that enters values that increase by .5 each iteration

# Exercise 4
def add_toppings():           #how can I make this code less repetitive?
    topping_list = []
    topping = input("What topping would you like to add?")
    while(topping != "quit"):
        topping_list.append(topping)
        print("We'll add that topping to your pizza")
        topping = input("What topping would you like to add?")
        topping_list.append(topping)
        print(topping_list)

# add_toppings()


# Exercise 6
def print_list():
    list = ["here", 'are', 'some', 'list', 'items']
    for item in list:
        print(item)


# # Exercise 7

def family_tickets():
    family = ["father", "mother", "brother", "sister"]
    for member in family:
        age = input("What is your age?")
        if age < 3:
            print("Your ticket is free")
            break
        elif age < 13:
            print("Your ticket is $10")
            break
        else:
            print("Your ticket is $15")
            break


# Exercise 8

def print_even_index():
    new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for item in new_list:
        if new_list.index(item) % 2 == 0:
            print(item)


# print_even_index

# Exercise 9

teens_allowed = []
def check_age_entry():
    teens = ["Jen", "Rob", "Bill", "Claire", "Maya"]
    for person in teens:
        age = input("Hi {}, how old are you? ".format(person))
        if(16 <= int(age) <= 21):
            teens_allowed.append(person)
    print("These people are allowed to see the movie: ", teens_allowed)

# check_age_entry()


# Exercise 10

def if_over_16():
    teens = ["Jen", "Rob", "Bill", "Claire", "Maya"]
    underage_teens = []
    for person in teens:
        age = input("Hi {}, how old are you? ".format(person))
        if (int(age) < 16):
            underage_teens.append(person)
    allowed_teens = [x for x in teens if x not in underage_teens]
    print(allowed_teens)


# if_over_16()


