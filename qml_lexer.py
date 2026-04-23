"""
Lexer Class

Owner: Cam
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
    Purpose:
        Scan QML source -> return list of Tokens

    Discard whitespace tokens. Strip TEXT tokens of whitespace
    in front & behind, then add to list.
    """
    
    tokens = []

    for match in MASTER_PATTERN.finditer(source):
        token_type = match.lastgroup
        token_value = match.group()

        # Ignore whitespace between tags
        if token_type == "WHITESPACE":
            continue

        if token_type == "TEXT":
            stripped = token_value.strip()
            # Whitespace-only node is discarded
            if stripped == "":
                continue
            tokens.append(Token(token_type, stripped))
            continue

        tokens.append(Token(token_type, token_value))

    return tokens