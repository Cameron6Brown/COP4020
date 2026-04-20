"""
Token Object Class

Owner: Jackson
"""

class Token:
    def __init__(self, type, value):
        self.type = type # Token category string ("TEXT", "WHITESPACE", etc)
        self.value = value # Token value string check to match source ("quiz", "question", "title", etc)
    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"