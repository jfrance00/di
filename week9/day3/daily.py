example = "I am an example text! Use me to test all of your methods on text to see if you know what you are doing and can manipulate the text"

class Text:
    def __init__(self, string):
        self.string = string
        self.string_as_list = string.split(" ")

    def word_frequency(self, word):
        counter = 0
        for item in self.string_as_list:
            if item == word:
                counter += 1
        return counter


    def most_common_word(self):
        counter = dict()
        occurances = 0
        for word in self.string_as_list:
            counter[word] = counter.get(word, 0) + 1
            if counter[word] > occurances:
                most_common_word = word
        return most_common_word


    def unique_words(self):
        unique_words = []
        for word in self.string_as_list:
            if word not in unique_words:
                unique_words.append(word)
        return unique_words

    @classmethod
    def text_file(cls):
        new_file = open("text_stat.txt", 'a')
        return new_file



class TextModification(Text):
    def no_punc(self):
        punc = ['.', ',', '!', '?']
        new_string = ""
        for char in self.string:
            if char not in punc:
                new_string = new_string + char
        return new_string

    def no_stop_words(self):
        relevant_word_list = []
        stop_words = open("stop_words.txt", 'r').read()
        stop_words_list = stop_words.split('\n')
        for word in self.string_as_list:
            if word not in stop_words_list:
                relevant_word_list.append(word)
        return relevant_word_list

    def no_special_chars(self):
        special_char = ['.', ',', '!', '?', '@', '#', '$','%','^','&','*','(',')','-','+','_','=',':',';',"'",'"','/']
        new_string = ""
        for char in self.string:
            if char not in special_char:
                new_string = new_string + char
        return new_string

my_text = TextModification(example)

# print(my_text.most_common_word())
print(my_text.no_special_chars())
# print(my_text.no_stop_words())
Text.text_file()