from src.dart_parser_generator import DartParserGenerator
from src.endian import Endian
from src.python_parser_generator import PythonParserGenerator
from src.language import Language


class ParserGeneratorFactory:
    @staticmethod
    def create(language: Language, endian: Endian):

        if language is Language.PYTHON:
            return PythonParserGenerator(endian)
        elif language is Language.DART:
            return DartParserGenerator(endian)
        else:
            raise NotImplementedError
