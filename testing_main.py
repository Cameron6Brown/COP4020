from qml_serializer import Serialize
from qml_ast_nodes import Quiz, Question, Option

s1 = Serialize("quiz")
quest1 = Question("What is the power house of the cell?", 
    {Option("Mitochondria", True), 
    Option("Cytoplasm"),
    Option("Nucleus"),
    Option("Golgi")})
quest2 = Question("What is the core of the cell?", 
    {Option("Mitochondria"), 
    Option("Cytoplasm"),
    Option("Nucleus", True),
    Option("Golgi")})
quiz = Quiz("Cell Test", {quest1, quest2})

s1.serialize_quiz(quiz)
print(quiz.to_dict())