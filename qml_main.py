"""
Main Driver File
"""

from qml_lexer import tokenize
from qml_parser import parse
from qml_serializer import serialize

source = open("midterm.quiz").read()
tokens = tokenize(source)
ast = parse(tokens)
output = serialize(ast)
print(output)