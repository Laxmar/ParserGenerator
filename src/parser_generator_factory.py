from src.dart_parser_generator import DartParserGenerator
from src.python_parser_generator import PythonParserGenerator
from src.language import Language


class ParserGeneratorFactory:

    __switcher = {
        Language.PYTHON: PythonParserGenerator(),
        Language.DART: DartParserGenerator()
    }

    @staticmethod
    def create(language: Language):
        generator = ParserGeneratorFactory.__switcher.get(language, None)
        if generator is None:
            raise NotImplementedError
        return generator

