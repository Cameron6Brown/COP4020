"""
Main Driver File

To use this transpiler, 
format cmd line input as:

python qml_main.py <filename>
"""

import sys
from qml_lexer import tokenize
from qml_parser import parse
from qml_serializer import serialize


# =========================
# Semantic Validation
# =========================
def validate(quiz):
    for q in quiz.questions:
        correct_count = sum(o.correct for o in q.options)

        if correct_count == 0:
            raise Exception("Question has no correct answer")

        if correct_count > 1:
            raise Exception("Question has multiple correct answers")


# =========================
# Main Driver
# =========================
def run_file(filename):
    if not filename.endswith(".quiz"):
        print(f"Skipping invalid file type: {filename}")
        return

    try:
        with open(filename, "r", encoding="utf-8") as f:
            source = f.read()

        # Lexical analysis
        tokens = tokenize(source)

        # Parsing (safe wrapper inside parser)
        ast = parse(tokens)

        # Semantic validation
        validate(ast)

        # Output generation
        output_file = filename.replace(".quiz", ".json")
        serialize(output_file, ast)

        print(f"Output written to {output_file}.")

    except Exception as e:
        print(f"Error in {filename}: {e}")


# =========================
# Entry Point
# =========================
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python qml_main.py <filename(s)>")
        sys.exit(1)

    for filename in sys.argv[1:]:
        run_file(filename)