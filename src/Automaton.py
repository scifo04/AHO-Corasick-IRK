from typing import List
import Util

class Node:
    letter: str
    children: list
    id: int
    level: int
    isFinish: bool

    count = 0

    def __init__ (self, letter, level):
        self.letter = letter
        self.children = []
        self.counter = Node.count
        self.failure_link = None
        self.level = level
        self.isFinish = False
        Node.count += 1

    def connect (self, node):
        self.children.append(node)

    def findInChildren(self, letter):
        for i in range(len(self.children)):
            if self.children[i].letter == letter:
                return i
        return -1

    def construct_tree(self,pattern: str, stretch: int, level: int):
        res = self.findInChildren(pattern[0:stretch])
        # print(pattern[0:stretch])
        if res == -1:
            newNode = Node(pattern[0:stretch],level)
            self.connect(newNode)
            if (len(pattern) > stretch):
                self.children[len(self.children)-1].construct_tree(pattern,stretch+1,level+1)
        else:
            if (len(pattern) > stretch):
                self.children[res].construct_tree(pattern,stretch+1,level+1)

    def print_tree(self):
        print(self,self.failure_link,self.letter,self.failure_link.letter,self.level)
        for i in range(len(self.children)):
            self.children[i].print_tree()

    def get_prefix(self, text: str, liste: list):
        for i in range(len(self.children)):
            liste.append(self.children[i].get_prefix_support(text,liste))
        return liste
    
    def get_prefix_support(self, text: str, liste: list):
        text = self.letter
        if (len(self.children) == 0):
            liste.append(text)
        else:
            liste.append(text)
            for i in range(len(self.children)):
                self.children[i].get_prefix_support(text,liste)

    def get_address(self,liste:list):
        liste.append(self)
        for i in range(len(self.children)):
            self.children[i].get_address(liste)
        return liste
    
    def find_node(self,text:str):
        newNode = None
        if (self.letter == text):
            return self
        else:
            for i in range(len(self.children)):
                newNode = self.children[i].find_node(text)
            return newNode

class Automaton:
    root: Node
    patterns: List[str]
    address = List[Node]
    prefix = List[str]
    def __init__ (self, patterns: List[str]):
        Node.count = 0
        self.root = Node("",0)
        self.root.failure_link = self.root
        self.patterns = patterns
        self.construct_branch()
        self.prefix = self.get_prefix()
        for i in patterns:
            self.prefix.remove(i)
        self.address = self.root.get_address([])
        self.get_failure_link()
        self.print_tree()

    def construct_branch (self):
        for pattern in self.patterns:
            self.root.construct_tree(pattern,1,1)

    def print_tree(self):
        self.root.print_tree()

    def get_prefix(self):
        liste = self.root.get_prefix("",[])
        cleaned_liste = [item for item in liste if item is not None]
        return cleaned_liste

    def find_node(self,text:str):
        return self.root.find_node(text)
    
    def get_failure_link(self):
        for i in range(1,len(self.address)):
            match = Util.find_match(Util.get_suffix(self.address[i].letter),self.prefix)
            print(match,self.address[i].letter)
            self.address[i].failure_link = self.find_list(match)
            if self.address[i].failure_link is None:
                self.address[i].failure_link = self.address[0]

    def find_list(self,match:str):
        for i in range(len(self.address)):
            if (self.address[i].letter == match):
                return self.address[i]
        return None
    
    def create_directed_graphs(self):
        liste = []
        for i in range(len(self.address)):
            for j in range(len(self.address[i].children)):
                liste.append((self.address[i].letter,self.address[i].children[j].letter))
            liste.append((self.address[i].letter,self.address[i].failure_link.letter))
        liste = list(set(liste))
        return liste