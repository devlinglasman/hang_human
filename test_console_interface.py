import pytest

from console_interface import *

from StringIO import StringIO

def mock_input_function():
    return "a"

class TestConsoleInterface():

    def test_welcome_message(self):
        output_stream = StringIO()
        console_interface = ConsoleInterface(output_stream)
        console_interface.welcome_message()

        expected_output = "Welcome to Hang_Human! You have 10 guesses to figure out the secret word! Good luck!"
        
        assert output_stream.getvalue() == expected_output

    def test_present_converted_word(self):
        output_stream = StringIO()
        console_interface = ConsoleInterface(output_stream)
        console_interface.present_converted_word("___")

        expected_output = "Word: ___"
        
        assert output_stream.getvalue() == expected_output

    def test_get_user_guess(self):
        console_interface = ConsoleInterface(get_input=mock_input_function)

        assert console_interface.get_user_guess() == "a"

