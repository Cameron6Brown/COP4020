"""
Parser

Contains:
    class Parse

Owner: Cameron
"""

from qml_token import Token
from qml_ast_nodes import Quiz, Question, Option


# =========================
# Token Definitions (FIXED DESIGN)
# Using (type, value) tuples instead of Token objects
# =========================
QUIZ_OPEN = ("TAG_OPEN", "<quiz>")
QUIZ_CLOSE = ("TAG_CLOSE", "</quiz>")
TITLE_OPEN = ("TAG_OPEN", "<title>")
TITLE_CLOSE = ("TAG_CLOSE", "</title>")
QUESTION_OPEN = ("TAG_OPEN", "<question>")
QUESTION_CLOSE = ("TAG_CLOSE", "</question>")
TEXT_OPEN = ("TAG_OPEN", "<text>")
TEXT_CLOSE = ("TAG_CLOSE", "</text>")
OPTION_OPEN = ("OPTION_OPEN", "<option>")
OPTION_OPEN_CORRECT = ("OPTION_OPEN_CORRECT", '<option correct="true">')
OPTION_CLOSE = ("OPTION_CLOSE", "</option>")


# =========================
# Parser State
# =========================
class ParserState:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def current(self):
        if self.index >= len(self.tokens):
            raise Exception("Unexpected end of input")
        return self.tokens[self.index]

    def advance(self):
        self.index += 1

    def expect(self, expected):
        token = self.current()

        if (token.type, token.value) != expected:
            raise Exception(
                f"Expected {expected}, got ({token.type}, {token.value}) at index {self.index}"
            )

        self.advance()


# =========================
# SAFE PARSE WRAPPER
# =========================
def parse(tokens):
    try:
        state = ParserState(tokens)
        return quiz(state)
    except Exception as e:
        raise Exception(f"[Parse Error] {e}")


# =========================
# HELPERS
# =========================
def is_question(state):
    t = state.current()
    return (t.type, t.value) == QUESTION_OPEN


def is_option(state):
    t = state.current()
    return (t.type, t.value) == OPTION_OPEN or (t.type, t.value) == OPTION_OPEN_CORRECT


# =========================
# quiz
# =========================
def quiz(state):
    state.expect(QUIZ_OPEN)

    title_text = title(state)

    questions = []

    while is_question(state):
        questions.append(question(state))

    state.expect(QUIZ_CLOSE)

    return Quiz(title_text, questions)


# =========================
# title
# =========================
def title(state):
    state.expect(TITLE_OPEN)

    if state.current().type != "TEXT":
        raise Exception(f"Expected TEXT in title, got {state.current()}")

    value = state.current().value
    state.advance()

    state.expect(TITLE_CLOSE)

    return value


# =========================
# question
# =========================
def question(state):
    state.expect(QUESTION_OPEN)

    q_text = text(state)

    options = []

    while is_option(state):
        options.append(option(state))

    if len(options) < 2:
        raise Exception("Question must have at least 2 options")

    state.expect(QUESTION_CLOSE)

    return Question(q_text, options)


# =========================
# text
# =========================
def text(state):
    state.expect(TEXT_OPEN)

    if state.current().type != "TEXT":
        raise Exception(f"Expected TEXT, got {state.current()}")

    value = state.current().value
    state.advance()

    state.expect(TEXT_CLOSE)

    return value


# =========================
# option
# =========================
def option(state):
    token = state.current()
    key = (token.type, token.value)

    if key == OPTION_OPEN_CORRECT:
        correct = True
    elif key == OPTION_OPEN:
        correct = False
    else:
        raise Exception(f"Invalid option token: {token}")

    state.advance()

    if state.current().type != "TEXT":
        raise Exception(f"Expected TEXT in option, got {state.current()}")

    value = state.current().value
    state.advance()

    state.expect(OPTION_CLOSE)

    return Option(value, correct)
