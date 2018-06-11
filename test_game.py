import pytest

from game import *

class TestGame():

    def test_convert_word1(self):
        game = Game(["c", "r", "a"])
        assert game.convert_word() == "___"

    def test_convert_word2(self):
        game = Game("devlin")
        assert game.convert_word() == "______"

    def test_convert_word3(self):
        game = Game("crafter")

        game.add_character_to_chosen_characters("a")

        assert game.convert_word() == "__a____"

    def test_character_present_is_true(self):
        game = Game("")
        assert game.character_present("crafter", "a") == True

    def test_character_present_is_false(self):
        game = Game("")
        assert game.character_present("crafter", "x") == False

    def test_add_character_to_chosen_characters1(self):
        game = Game("")

        game.add_character_to_chosen_characters("a")

        assert game.get_chosen_characters() == ["", "a"]

    def test_add_character_to_chosen_characters2(self):
        game = Game("")

        game.add_character_to_chosen_characters("a")
        game.add_character_to_chosen_characters("b")

        assert game.get_chosen_characters() == ["", "a", "b"]

    def test_game_lost(self):
        game = Game("crafter")

        game.set_guesses_left(0)

        assert game.game_lost() == True

    def test_game_lost(self):
        game = Game("crafter")

        assert game.game_lost() == False 

    def test_minus_guess(self):
        game = Game("crafter")

        game.minus_guess()

        assert game.get_guesses_left() == 9
