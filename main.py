from game import *
from console_interface import *

class GameRunner():

    def __init__(self, game, console_interface):
        self.game = game
        self.console_interface = console_interface

    def run_game(self):
        console_interface.welcome_message()
        secret_word = game.convert_word()

        while "_" in secret_word:
            console_interface.present_converted_word(secret_word)
            console_interface.ask_for_letter_choice()
            chosen_letter = console_interface.get_user_guess()
            game.add_character_to_chosen_characters(chosen_letter)
            secret_word = game.convert_word()
            console_interface.present_converted_word(secret_word)
        else:
            print "You won!"

    def get_console_interface(self):
        return console_interface

game = Game("crafter")
console_interface = ConsoleInterface()
game_runner = GameRunner(game, console_interface)

game_runner.run_game()
