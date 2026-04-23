# COP4020 QML Transpiler
Programming Language

## EBNF

```
quiz       = "<quiz>", title, question, {question}, "</quiz>" ;
title      = "<title>", TEXT, "</title>" ;
question   = "<question>", text, option, option, {option}, "</question>" ;
text       = "<text>", TEXT, "</text>" ;
option     = "<option", [whitespace, attribute], ">", TEXT, "</option>" ;
attribute  = 'correct="true"' ;
whitespace = " " | "\n" | "\t" | "\r" ;
TEXT       = { character } ;
character  = letter | digit | punctuation | whitespace ;
letter     = "a" | ... | "z" | "A" | ... | "Z" ;
digit      = "0" | ... | "9" ;
punctuation = "." | "," | "?" | "!" | "-" | "'" ;
```

## Recursive-Descent Parser & AST Structure

This module is responsible for parsing the token stream produced by `qml_lexer.py` and validating the structure of a QML file against the defined grammar. It focuses strictly on syntax and AST construction, including:

- `qml_parser.py`: Implements a recursive-descent parser that consumes tokens, matches grammar rules, and builds AST nodes.
- `qml_ast_nodes.py`: Defines AST node classes such as `Quiz`, `Question`, and `Option`.
- Syntax validation: Ensures required elements are present and nested correctly according to the grammar.

The parser does not perform semantic validation such as answer correctness; that is handled separately in `qml_main.py`.

## Usage

Run the parser and serializer from the project root with a `.quiz` file:

```bash
python qml_main.py cell.quiz
```

This will:
- tokenize the input with `qml_lexer.py`
- parse the token stream with `qml_parser.py`
- validate the AST structure and quiz semantics in `qml_main.py`
- write the output JSON to `cell.json`

You can pass multiple `.quiz` files:

```bash
python qml_main.py cell.quiz midterm.quiz
```

If you want the generated JSON printed to the terminal, add `--stdout`:

```bash
python qml_main.py cell.quiz --stdout
```

This prints the parsed JSON to the terminal while still writing `cell.json`.
