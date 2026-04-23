"""
Main Driver File
"""

from qml_parser import Parse
from qml_lexer import Lexer
from qml_serializer import Serialize

source = open("midterm.quiz").read()
tokens = Parse(source).parse()
ast = Lexer(tokens)
output = Serialize(ast)
print(output)