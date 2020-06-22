from googletrans import Translator

translator = Translator()

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

trans_dict = {}
for word in french_words:
    trans_dict[word] = translator.translate(word).text
print(trans_dict)
