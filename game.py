class Game():

    def __init__(self, word_to_guess):
        self.word_to_guess = word_to_guess

    def hide_word(self, word):
        hidden_word = len(word) * "_"
        return hidden_word

    def character_present(self, word, char):
        return char in word

