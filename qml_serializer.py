"""
Serializer Class

Contains:
    class Serialize

Owner: Bryce
"""

import json
from qml_ast_nodes import Quiz, Question, Option

class Serialize:
    def __init__(self, filename):
        self.filename = filename 

    def serialize_quiz(self, quiz):
        with open(self.filename, 'w') as file:
            json.dump(quiz.to_dict(), file, indent=4, ensure_ascii=False)