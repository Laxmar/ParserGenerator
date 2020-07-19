from src.endian import Endian


class AbstractParserGenerator:
    def __init__(self, endian: Endian):
        self.endian = endian

    def generate_class(self, struct_dto):
        pass

    def generate_parse_function(self, struct_dto):
        pass
