from JsonGetter import QueryUnpacker
from Automaton import Automaton
from typing import List

class AHOCorasick:
    file_path: str
    solution_list: List[str]
    unpacker: QueryUnpacker
    automaton: Automaton
    hashmap: dict
    start_track: int
    end_track: int
    to_graph: List[str]

    def __init__ (self, path):
        self.file_path = path
        self.unpacker = QueryUnpacker(path)
        self.solution_list = []
        self.hashmap = {}
        for i in range(len(self.unpacker.patterns)):
            self.unpacker.patterns[i] = self.unpacker.patterns[i].lower()
            self.hashmap[self.unpacker.patterns[i]] = []
        self.automaton = Automaton(self.unpacker.patterns)
        self.unpacker.text = self.unpacker.text.lower()
        self.solve()
        for i in self.hashmap:
            print(i,self.hashmap[i])
        self.to_graph = self.automaton.create_directed_graphs()
        
    def solve (self):
        text = self.unpacker.text
        tree = self.automaton.root
        fail = self.automaton.root.failure_link
        for i in range(len(self.unpacker.text)):
            res = tree.findInChildren(text[i-tree.level:i+1])
            print(res, text[i-tree.level:i+1])
            saved_string = text[i-tree.level:i+1]
            if (res != -1 and len(tree.children) > 0):
                fail = tree.children[res].failure_link
                tree = tree.children[res]
                if (saved_string in self.unpacker.patterns):
                    self.hashmap[saved_string].append((i-len(saved_string)+1,i))
                    if (len(tree.children) == 0):
                        tree = tree.failure_link
                    print("APPEND")
            else:
                while True:
                    if (tree.letter == self.automaton.root.letter):
                        res = tree.findInChildren(text[i-tree.level:i+1])
                        print(res, text[i-tree.level:i+1])
                        saved_string = text[i-tree.level:i+1]
                        if (res != -1 and len(tree.children) > 0):
                            fail = tree.children[res].failure_link
                            tree = tree.children[res]
                            if (saved_string in self.unpacker.patterns):
                                self.hashmap[saved_string].append((i-len(saved_string)+1,i))
                                tree = tree.failure_link
                                print("APPEND")
                        break

                    tree = fail
                    res = tree.findInChildren(text[i-len(saved_string):i+1])
                    if (res != -1 and len(tree.children) > 0):
                        tree = tree.children[res]
                        fail = tree.failure_link
                        if (saved_string in self.unpacker.patterns):
                            self.hashmap[saved_string].append((i-len(saved_string)+1,i))
                            tree = tree.failure_link
                            print("APPEND")
                        break
                    else:
                        fail = tree.failure_link