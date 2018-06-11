class Game():

    def __init__(self, word_to_guess):
        self.word_to_guess = word_to_guess
        self.chosen_characters = []

    def hide_word(self, word):
        hidden_word = len(word) * "_"
        return hidden_word

    def character_present(self, word, char):
        return char in word

    def add_character_to_chosen_characters(self, char):
        self.chosen_characters.append(char)

    def get_chosen_characters(self):
        return self.chosen_characters



