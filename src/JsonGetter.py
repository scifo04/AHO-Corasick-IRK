import json

class QueryUnpacker:
    text: str
    patterns: list

    def __init__(self,path):
        f = open(path,encoding="utf-8")
        data = json.load(f)
        self.text = data["text"]
        self.patterns = data["patterns"]
        f.close()