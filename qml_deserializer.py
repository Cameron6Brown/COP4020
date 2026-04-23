import json

def deserialize(filename):
    with open(filename) as f:
        return json.load(f)