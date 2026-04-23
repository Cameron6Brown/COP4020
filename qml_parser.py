"""
Parser

Contains:
    class Parse

Owner: Bryce
"""

from qml_token import Token

class Parse:
    def __init__(self, source):
        self.source = source
        self.tokens = []

    def parseSource(self):

        for char in self.source:
            match char:
                case '<':
                    continue

        return self.tokens

