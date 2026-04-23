"""
Main Driver File

To use this transpiler, 
format cmd line input as:

python qml_main.py <filename>
"""

import sys
<<<<<<< HEAD
import json
=======
>>>>>>> 00f08925591f042d99a647d4f8a2f61ca24772c3
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
<<<<<<< HEAD
def run_file(filename, print_to_terminal=False):
=======
def run_file(filename):
>>>>>>> 00f08925591f042d99a647d4f8a2f61ca24772c3
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

<<<<<<< HEAD
        if print_to_terminal:
            print(json.dumps(ast.to_dict(), indent=4, ensure_ascii=False))

=======
>>>>>>> 00f08925591f042d99a647d4f8a2f61ca24772c3
        print(f"Output written to {output_file}.")

    except Exception as e:
        print(f"Error in {filename}: {e}")


# =========================
# Entry Point
# =========================
if __name__ == "__main__":
    if len(sys.argv) < 2:
<<<<<<< HEAD
        print("Usage: python qml_main.py <filename(s)> [--stdout]")
        sys.exit(1)

    print_output = "--stdout" in sys.argv
    filenames = [f for f in sys.argv[1:] if f != "--stdout"]

    if not filenames:
        print("No input files provided.")
        sys.exit(1)

    for filename in filenames:
        run_file(filename, print_to_terminal=print_output)
=======
        print("Usage: python qml_main.py <filename(s)>")
        sys.exit(1)

    for filename in sys.argv[1:]:
        run_file(filename)
>>>>>>> 00f08925591f042d99a647d4f8a2f61ca24772c3
