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

def check_letters(char):
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    part_of_message = False
    if char in valid_chars:
        part_of_message = True
    return part_of_message

def record_letter(char):
    global hidden_message
    hidden_message = hidden_message + char
    print(hidden_message)
    return hidden_message

def square_lists(list):
    list.append(' ')
    return list


def scan_matrix(matrix):
    loop_length = longest_list(matrix)
    loop = 0
    while loop < loop_length:
        print(" ")
        for index, item in enumerate(matrix):
            if (len(item) < 3):
                square_lists(item)
            print("index: {}, loop: {}".format(index, loop))
            value  = item[loop]   #gets an error that index out of range
            print(value)
            if (check_letters(value)):
                message = record_letter(value)
        loop += 1
    print(message)





#scan matrix[0][i] and record letters
#scan matrix[1][j] record relev letters
#scan matrix[2][k] record letters

scan_matrix(matrix)