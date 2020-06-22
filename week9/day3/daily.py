
class Text:
    def __init__(self, string):
        self.string = string
        self.string_as_list = string.split(" ")


    def word_frequency(self, word):
        counter = 0
        for item in self.string_as_list:
            if item.lower() == word.lower():
                counter += 1
        return counter

    def most_common_word(self):
        counter = dict()
        occurences = 0
        for i, word in enumerate(self.string_as_list):
            if word not in counter:
                counter[word] = counter.get(word, 1)
            else:
                counter[word] += 1
            if counter[word] > occurences:
                most_common_word = word
                occurences = counter[word]
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
            if word.lower() not in stop_words_list:
                relevant_word_list.append(word)
        relevent_word_str = " ".join(relevant_word_list)
        return relevent_word_str

    def no_special_chars(self):
        special_char = ['.', ',', '!', '?', '@', '#', '$','%','^','&','*','(',')','-','+','_','=',':',';',"'",'"','/']
        new_string = ""
        for char in self.string:
            if char not in special_char:
                new_string = new_string + char
        return new_string


my_text = TextModification(open('the_stranger.txt', 'r').read())
refine_text = my_text.no_stop_words()
my_refined_text = TextModification(refine_text)
print(my_refined_text.most_common_word())


