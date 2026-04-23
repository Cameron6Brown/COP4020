"""
Main Driver File

To use this transpiler, 
format cmd line input as:

python qml_main.py <filename>
"""

import sys
from qml_lexer import tokenize
from qml_parser import parse
from qml_serializer import Serialize


source = open(sys.argv[1]).read()
tokens = tokenize(source)
ast = parse(tokens)
output_file = sys.argv[1].replace(".quiz", ".json")
Serialize(output_file, ast)
print(f"Output written to {output_file}.")