# Get a string from the user. The user must provide a string that is 10 characters long.
# Swap some of the characters around, then print out this jumbled-up string to the user. Be sure to label it appropriately.

def check_first_letter(str):
    first_letter = str[0]
    print("The first letter is:", first_letter)
    return

def check_last_letter(str):
    last_letter = str[len(str)-1]
    print("The last letter is:", last_letter)
    return
#qwertyuiop
def build_string(str):
    add_letter = ""
    for i in str:
        print(add_letter + i)
        add_letter = add_letter+i
    return

def switch_letter(str):
    place_holder = str[0]
    new_str = str[2] + str[4] + str[6] + str[8] + str[0] + str[1] + str[3] + str[5] + str[7] +str[9]
    print(new_str)
    return


user_string = input("please enter a 10 character string ")
if (len(user_string) != 10):
    input("Make sure you string is 10 characters ")
else:
    check_first_letter(user_string)
    check_last_letter(user_string)
    build_string(user_string)
    switch_letter(user_string)
