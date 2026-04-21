"""
Serializer Class

Contains:
    class Serialize

Owner: Bryce
"""

import json
from qml_ast_nodes import Quiz, Question, Option

class Serialize:
    L_DELIMITERS = {'{', '['}
    R_DELIMITERS = {'}', ']'}
    COMMA = ','

    def __init__(self, filename):
        self.filename = filename 

    def serialize_quiz(self, quiz, overwrite=False):
        unformatted_data = json.dumps(repr(quiz))
        formatted_data = ""

        depth = 0
        for i in range(len(unformatted_data) - 1):
            if unformatted_data[i] in self.L_DELIMITERS or unformatted_data[i] in self.R_DELIMITERS or  unformatted_data[i] in self.COMMA:
                if unformatted_data[i] in self.R_DELIMITERS:
                    formatted_data += '\n'
                    for tab in range(depth):
                        formatted_data += '\t'
                    formatted_data += unformatted_data[i]
                    depth -= 1
                    continue

                formatted_data += unformatted_data[i]
                if unformatted_data[i+1] == self.COMMA:
                    continue

                formatted_data += '\n'
                for tab in range(depth):
                    formatted_data += '\t'
                depth += 1
                continue
            formatted_data += unformatted_data[i]

        print(formatted_data)


        