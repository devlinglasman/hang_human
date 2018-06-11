import sys

class ConsoleInterface(object):
    def __init__(self, out_stream=sys.stdout, get_input=raw_input):
        self._out_stream = out_stream
        self._get_input = get_input

    def welcome_message(self):
        self._out_stream.write("Welcome to Hang_Human! You have 10 guesses to figure out the secret word! Good luck!")

    def present_converted_word(self, converted_word):
        content = "Word: " + converted_word
        self._out_stream.write(content)

    def ask_for_letter_choice(self):
        self._out_stream.write("Please enter a letter.")

    def present_guesses_left(self, guesses_left):
        self._out_stream.write("You have " + guesses_left + " guesses left.")

    def lost_message(self):
        self._out_stream.write("You lost... now YOU will be hanged!")

    def won_message(self):
        self._out_stream.write("You won! You saved the human!")

    def get_user_guess(self):
        return self._get_input()


