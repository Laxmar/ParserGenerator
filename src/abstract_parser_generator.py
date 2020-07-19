from src.endian import Endian


class AbstractParserGenerator:
    def __init__(self, endian: Endian):
        self.endian = endian
        self.end_of_line = "\n"

    def generate_class(self, struct_dto):
        pass

    def generate_parse_function(self, struct_dto):
        pass
