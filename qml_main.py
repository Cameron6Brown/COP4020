"""
Main Driver File
"""

from qml_lexer import tokenize
from qml_parser import parse
from qml_serializer import serialize
from qml_ast_nodes import Quiz

source = open("cell.quiz").read()
tokens = tokenize(source)
ast: Quiz = parse(tokens)
output = serialize("cell.json", ast)
print(output)