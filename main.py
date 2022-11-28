import sys
from antlr4 import *

from XMLLexer import XMLLexer
from XMLParser import XMLParser
from XMLParserListener import XMLParserListener


class Validator():
    def __init__(self):
        self.files = "./files/"
        self.input = None
        self.code = ""

    def loadFile(self):
        if len(sys.argv) > 1:
            self.input = sys.argv[1]
            return True
        else:
            print("missing input file")
            return False

    def readFile(self):
        file = open(self.files + self.input, "rt")
        self.code = file.read()

    def validate(self):
        lexer = XMLLexer(InputStream(self.code))
        stream = CommonTokenStream(lexer)
        parser = XMLParser(stream)
        tree = parser.document()
        walker = ParseTreeWalker()
        listener = XMLParserListener()
        walker.walk(listener, tree)


if __name__ == '__main__':
    validator = Validator()
    if validator.loadFile():
        validator.readFile()
        validator.validate()
