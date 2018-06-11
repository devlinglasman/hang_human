class Game():

    def __init__(self, word_to_guess):
        self.word_to_guess = word_to_guess
        self.chosen_characters = [""]

    def convert_word(self):
        converted_word = []
        for char_in_word_to_guess in self.word_to_guess:
            if char_in_word_to_guess in self.chosen_characters:
                converted_word.append(char_in_word_to_guess)
            else: 
                converted_word.append("_")
        return ''.join(converted_word)

    def character_present(self, word, char):
        return char in word

    def add_character_to_chosen_characters(self, char):
        self.chosen_characters.append(char)

    def get_chosen_characters(self):
        return self.chosen_characters



