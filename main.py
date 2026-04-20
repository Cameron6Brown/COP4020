"""
Main Driver File
"""

from lexer import tokenize
from parser import parse
from serializer import serialize

source = open("midterm.quiz").read()
tokens = tokenize(source)
ast = parse(tokens)
output = serialize(ast)
print(output)