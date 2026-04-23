"""
Parser

Contains:
    class Parse

Owner: Bryce
"""

from qml_token import Token
from qml_ast_nodes import Quiz, Question, Option

QUIZ_OPEN = Token('TAG_OPEN', '<quiz>')
QUIZ_CLOSE = Token('TAG_CLOSE', '</quiz>')
TITLE_OPEN = Token('TAG_OPEN', '<title>')
TITLE_CLOSE = Token('TAG_CLOSE', '</title>')
QUESTION_OPEN = Token('TAG_OPEN', '<question>')
QUESTION_CLOSE = Token('TAG_CLOSE', '</question>')
TEXT_OPEN = Token('TAG_OPEN', '<text>')
TEXT_CLOSE = Token('TAG_CLOSE', '</text>')
OPTION_OPEN = Token('OPTION_OPEN', '<option>')
OPTION_OPEN_CORRECT = Token('OPTION_OPEN_CORRECT', '<option correct="true">')
OPTION_CLOSE = Token('OPTION_CLOSE', '</option>')

def parse(tokens):
    return quiz(tokens)

def quiz(tokens):
    if tokens[0] != QUIZ_OPEN:
        raise Exception("Invalid Token")
    
    tokens.pop(0)
    quiz_title = title(tokens)
    questions = [question(tokens)]
    while tokens[0] == QUESTION_OPEN:
        questions.append(question(tokens))

    if tokens[0] != QUIZ_CLOSE:
        raise Exception("Invalid Token")

    return Quiz(quiz_title, questions)

def title(tokens):
    if tokens[0] != TITLE_OPEN and tokens[1].type != 'TEXT' and tokens[2] != TITLE_CLOSE:
        raise Exception("Invalid Token")

    tokens.pop(0)
    text = tokens.pop(0).value
    tokens.pop(0)

    return text

def question(tokens):
    if tokens[0] != QUESTION_OPEN:
        raise Exception("Invalid Token")

    tokens.pop(0)
    question = text(tokens)
    tokens.pop(0)

    options = [option(tokens)]
    options.append(option(tokens)) # 2 or more questions
    while tokens[0] == OPTION_OPEN or tokens[0] == OPTION_OPEN_CORRECT:
        options.append(option(tokens))

    if tokens[0] != QUESTION_CLOSE:
        raise Exception("Invalid Token")

    return Question(question, options)

def text(tokens):
    if tokens[0] != TEXT_OPEN and tokens[1].type != 'TEXT' and tokens[2] != TEXT_CLOSE:
        raise Exception("Invalid Token")

    tokens.pop(0)
    text = tokens.pop(0).value
    tokens.pop(0)

    return text

def option(tokens):
    if tokens[0] != OPTION_OPEN and tokens[0] != OPTION_OPEN_CORRECT:
        raise Exception("Invalid Token")

    correct = tokens.pop(0) == OPTION_OPEN_CORRECT 

    if tokens[0].type != 'TEXT' and tokens[1] != OPTION_CLOSE:
        raise Exception("Invalid Token")

    tokens.pop(0)
    text = tokens.pop(0).value

    return Option(text, correct)