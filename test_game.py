import pytest

from game import *

class TestGame():

    def test_hide_word1(self):
        game = Game(["c", "r", "a"])

        assert game.hide_word() == ["_","_","_"]

    def test_hide_word2(self):
        game = Game("devlin")
        assert game.hide_word() == ["_", "_", "_", "_", "_", "_"]

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
