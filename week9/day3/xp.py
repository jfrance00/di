import random

def get_words_from_file():
    words = []
    with open("wordsfile.txt", "r") as f:
        return [line.replace('\n', '') for line in f]

def get_random_sentance(length):
    sentence = ""
    possible_new_words = get_words_from_file()
    index_options = len(possible_new_words)
    for word in range(length):
        new_word = possible_new_words[random.randint(0,index_options)]
        sentence += new_word + " "
    return sentence.lower()


def main():
    length = input("How long do you want your random sentence to be? ")
    try:
        length = int(length)
        print("Your random sentence " + "'" +get_random_sentance(length)+ "'")
    except:
        print("You did not enter a number. Cannot compute.")

main()


