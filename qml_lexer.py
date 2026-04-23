"""
Lexer Class

<<<<<<< HEAD
Owner: Cameron
=======
Owner: Cam
>>>>>>> 00f08925591f042d99a647d4f8a2f61ca24772c3
"""
import re
from qml_token import Token

# Tuples defined as (TOKEN_TYPE, regex_pattern)
# Ordered in decreasing specificity
# OPTION_OPEN_CORRECT must match TAG_OPEN, so we put it before TAG_OPEN

TOKEN_PATTERNS = [
    ("OPTION_OPEN_CORRECT", r'<option\s+correct="true">'),
    ("OPTION_CLOSE", r'</option>'),
    ("OPTION_OPEN", r'<option>'),
    ("TAG_CLOSE", r'</[a-zA-Z]+>'),
    ("TAG_OPEN", r'<[a-zA-Z]+>'),
    ("TEXT", r'[^<>]+'),
    ("WHITESPACE", r'[\s]'),
]

# One regex is made by merging all patterns via capturing groups
# "|" alternates left & right to keep order

MASTER_PATTERN = re.compile(
    "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_PATTERNS)
)

def tokenize(source: str) -> list:
    """
    Scan QML source -> return list of Tokens
    Now includes line and column tracking for better error reporting.
    """

    tokens = []

    for match in MASTER_PATTERN.finditer(source):
        token_type = match.lastgroup
        token_value = match.group()

        start = match.start()

        # Compute line number
        line = source.count("\n", 0, start) + 1

        # Compute column number
        last_newline = source.rfind("\n", 0, start)
        if last_newline == -1:
            column = start + 1
        else:
            column = start - last_newline

        # Ignore whitespace tokens
        if token_type == "WHITESPACE":
            continue

        if token_type == "TEXT":
            stripped = token_value.strip()
            if stripped == "":
                continue
            tokens.append(Token(token_type, stripped, line, column))
            continue

        tokens.append(Token(token_type, token_value, line, column))

    return tokens