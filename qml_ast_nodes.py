"""
AST Nodes

Contains:
    class Quiz
    class Question
    class Option

Owner: Jackson
"""

class Quiz:
    def __init__(self, title, questions):
        self.title = title # string for quiz title
        self.questions = questions # list of Question objects

    def to_dict(self):
        return {
            "title": self.title,
            "questions": [q.to_dict() for q in self.questions]
        }

    def __repr__(self):
        return f"Quiz(title={repr(self.title)},\
        questions={self.questions})"
    
class Question:
    def __init__(self, text, options):
        self.text = text # string for question text
        self.options = options # list for Option objects

    def to_dict(self):
        return {
            "text": self.text,
            "options": [o.to_dict() for o in self.options]
        }

    def __repr__(self):
        return f"Question(text={repr(self.text)},\
            options={self.options})"
    
class Option:
    def __init__(self, text, correct=False):
        self.text = text # string for option text
        self.correct = correct # boolean, default is false

    def to_dict(self):
        return{
            "text": self.text,
            "correct": self.correct
        }

    def __repr__(self):
        return f"Option(text={repr(self.text)},\
        correct={self.correct})"