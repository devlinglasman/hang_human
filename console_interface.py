import sys

class ConsoleInterface(object):
    def __init__(self, out_stream=sys.stdout, get_input=raw_input):
        self._out_stream = out_stream
        self._get_input = get_input

    def present_converted_word(self, converted_word):
        content = "Word: " + converted_word
        self._out_stream.write(content)

    def get_user_guess(self):
        return self._get_input()


