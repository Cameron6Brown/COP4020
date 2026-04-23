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
    
    index = 1
    quiz_title, index = title(tokens, index)

    q, index = question(tokens, index)
    questions = [q]
    while tokens[index] == QUESTION_OPEN:
        q, index = question(tokens, index)
        questions.append(q)

    if tokens[index] != QUIZ_CLOSE:
        raise Exception("Invalid Token")
    index += 1

    return Quiz(quiz_title, questions)

def title(tokens, index):
    if tokens[index] == TITLE_OPEN and tokens[index + 1].type == 'TEXT' and tokens[index + 2] == TITLE_CLOSE:
        index += 1
        text = tokens[index].value
        index += 2

        return [text, index]

    raise Exception("Invalid Token")


def question(tokens, index):
    if tokens[index] != QUESTION_OPEN:
        raise Exception("Invalid Token")

    index += 1
    question, index = text(tokens, index)
    o, index = option(tokens, index)
    options = [o]
    o, index = option(tokens, index)
    options.append(o) # 2 or more questions
    while tokens[index] == OPTION_OPEN or tokens[index] == OPTION_OPEN_CORRECT:
        o, index = option(tokens, index)
        options.append(o)

    if tokens[index] != QUESTION_CLOSE:
        raise Exception("Invalid Token")
    index += 1

    return [Question(question, options), index]

def text(tokens, index):
    if tokens[index] == TEXT_OPEN and tokens[index + 1].type == 'TEXT' and tokens[index + 2] == TEXT_CLOSE:
        index += 1
        text = tokens[index].value
        index += 2

        return [text, index]

    raise Exception("Invalid Token")


def option(tokens, index):
    if tokens[index] != OPTION_OPEN and tokens[index] != OPTION_OPEN_CORRECT:
        raise Exception("Invalid Token")

    correct = (tokens[index] == OPTION_OPEN_CORRECT)
    index += 1

    if tokens[index].type == 'TEXT' and tokens[index + 1] == OPTION_CLOSE:
        text = tokens[index].value
        index +=2

        return [Option(text, correct), index]

    raise Exception("Invalid Token")
