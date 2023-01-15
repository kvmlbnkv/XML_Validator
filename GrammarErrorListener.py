from antlr4.error.ErrorListener import ErrorListener
import sys


class GrammarErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        super().syntaxError(recognizer, offendingSymbol, line, column, msg, e)
        print("XML document is malformed and therefore dangerous")
        sys.exit()
