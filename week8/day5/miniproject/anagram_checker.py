
def collect_input():
    user_input = input("please enter a word: ")
    user_input = user_input.upper()                 # sets user input to all-caps
    user_input = user_input.strip()              # strips the input
    return user_input


class AnagramChecker():


    file = open("dictionary.txt", 'r')  #done - TODO parse to list (convert every string to upper just in case)
    dictionary = []
    for line in file:
        stripped_line = line.strip("\n")                # makes dictionary uniform
        stripped_line = stripped_line.upper()
        dictionary.append(stripped_line)

    file.close()


    def __init__(self):
        self.user_input = collect_input()
        while not self.is_valid_word():
            print("Word can only contain letters")
            self.user_input = collect_input()
        while not self.is_word_in_dict():
            print("Word not found. please try another word")
            self.user_input = collect_input()


    def is_valid_word(self):
        valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in self.user_input:
            if char not in valid_characters:
                return False
            else:
                return True

    def is_word_in_dict(self):
        if self.user_input in self.dictionary:
            return True
        else:
            return False


    def got_anagrams(self):
        anagrams = []
        for item in self.dictionary:
            if sorted(item) == sorted(self.user_input):
                    anagrams.append(item)
        return anagrams


play = AnagramChecker()
print(play.got_anagrams())