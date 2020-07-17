from src import struct_dto
from src.abstract_parser_generator import AbstractParserGenerator


class PythonParserGenerator(AbstractParserGenerator):
    def __init__(self):
        self.body = ""

    # TODO pass params for formating
    def generate_class(self, struct_dto: struct_dto):
        self.create_file_header(struct_dto.name)

        self.body += "\tdef __init__(self):" + "\n"
        for variable in struct_dto.variables:
            self.body += "\t\t" + variable.name + " = " + "0" + "\n"

        print(self.body)

    def generate_parse_function(self, struct_dto):
        pass

    def create_file_header(self, struct_name):
        self.body = "class " + struct_name + ":" + "\n"
