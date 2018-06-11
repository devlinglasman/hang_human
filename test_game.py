import pytest

from game import *

class TestGame():

    def test_hide_word1(self):
        game = Game()
        assert game.hide_word("crafter") == "_______"

    def test_hide_word2(self):
        game = Game()
        assert game.hide_word("devlin") == "______"
