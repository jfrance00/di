from anagram_checker import AnagramChecker


def show_menu():
    find_anagrams = input("would you like to find anagrams? Type yes to find or exit to quit")
    if find_anagrams == 'yes':
        check_anagram = AnagramChecker()
    elif find_anagrams == 'exit':
        print("no anagram for you")



show_menu()