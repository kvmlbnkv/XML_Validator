import sys
from antlr4 import *
import xmlschema

from XMLLexer import XMLLexer
from XMLParser import XMLParser
from XMLParserListener import XMLParserListener


class Validator():
    def __init__(self):
        self.files = "./files/"
        self.schemas = "./schemas/"
        self.input = None
        self.schema = None
        self.code = ""
        self.with_schema = False

    def loadFiles(self):
        if len(sys.argv) == 2:
            self.input = sys.argv[1]
            print("No schema attached.")
            return True
        elif len(sys.argv) == 3:
            self.input = sys.argv[1]
            self.schema = xmlschema.XMLSchema(self.schemas + sys.argv[2])
            self.with_schema = True
            return True
        else:
            print("Missing input file")
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

        if self.with_schema:
            if self.schema.is_valid(self.files + self.input):
                print("XML file seems to have correct syntax and is compatible with given schema.")
            else:
                print("XML file not compatible with given schema.")
        else:
            print("XML file seems to have correct syntax. Please provide XML schema file (XSD) in order to fully check the file.")

if __name__ == '__main__':
    validator = Validator()
    if validator.loadFiles():
        validator.readFile()
        validator.validate()
