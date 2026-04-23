"""
Token Object Class

Owner: Jackson
"""

class Token:
    def __init__(self, type, value, line=None, column=None):
        self.type = type
        self.value = value
        self.line = line
        self.column = column