class CheckPalindrome:
    def __init__(self, word):
        self.word = word

    def flip_word(self):
        flipped = ''
        for letter in self.word:
            flipped = letter + flipped
        return flipped

    def check_palindrome(self):
        if self.word == self.flip_word():
            print(f'{self.word} is a Palindrome!')
            return True
        else:
            print(f'{self.word} is not a palindrome :( ')
            return False




check = CheckPalindrome("radar")
print(check.check_palindrome())

check2 = CheckPalindrome("word")
print(check2.check_palindrome())


