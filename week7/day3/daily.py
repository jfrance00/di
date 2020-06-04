matrix = [
    [ '7' ,' ', '3' ],
    ['T','s','i'],
    ['h','%','x'],
    ['i',' ','#'],
    ['s', 'M'],
    ['$','a'],
    ['#','t','%'],
    ['i','r','!'],
]

hidden_message = " "

def longest_list(matrix):
    longest = matrix[0]
    for item in matrix:
        if len(item) > len(longest):
            longest = item
    return len(longest)


def square_lists(list):
    list.append(' ')
    return list


def is_value_letter(char):
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    part_of_message = False
    if char in valid_chars:
        part_of_message = True
    return part_of_message


def is_value_other(char):
    is_space = False
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    if (char not in valid_chars):
        is_space = True
    return is_space


def record_letter(char):
    global hidden_message
    print("adding {}".format(char))
    hidden_message = hidden_message + char
    return hidden_message


def record_space(char):
    global hidden_message
    print("adding space")
    space = " "
    hidden_message = hidden_message + space
    return hidden_message



def scan_matrix(matrix):
    loop_length = longest_list(matrix)
    loop = 0
    while loop < loop_length:
        for index, item in enumerate(matrix):
            if (len(item) < 3):
                square_lists(item)
            value = item[loop]
            print("value being checked is: ", value)
            if (is_value_letter(value)):
                message = record_letter(value)
            elif (is_value_other(value)):
                message = record_space(value)
        loop += 1
    print(message)





#scan matrix[0][i] and record letters
#scan matrix[1][j] record relev letters
#scan matrix[2][k] record letters

scan_matrix(matrix)