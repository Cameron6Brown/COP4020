"""
Serializer Class

Contains:
    class Serialize

Owner: Bryce
"""

import json
from qml_ast_nodes import Quiz, Question, Option

def serialize(self, filename, quiz):
    with open(filename, 'w') as file:
        json.dump(quiz.to_dict(), file, indent=4, ensure_ascii=False)