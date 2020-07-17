from enum import Enum

from src import struct_dto
from src.abstract_parser_generator import AbstractParserGenerator
from src.variable_dto import VariableType, VariableDto


class DartVariableType(Enum):

    int = "int"
    double = "double"
    bool = "bool"


    @staticmethod
    def convert(variable: VariableDto):
        # TODO format variable type if custom? or format after extraction?
        switcher = {
            VariableType.uint8: DartVariableType.int,
            VariableType.uint16: DartVariableType.int,
            VariableType.uint32: DartVariableType.int,

            VariableType.int8: DartVariableType.int,
            VariableType.int16: DartVariableType.int,
            VariableType.int32: DartVariableType.int,

            VariableType.float: DartVariableType.double,
            VariableType.double: DartVariableType.double,
            VariableType.bool: DartVariableType.bool
        }
        return switcher.get(variable.type, variable.type)


class DartParserGenerator(AbstractParserGenerator):

    # TODO pass params for formating and endian implement in AbstractParserGenerator
    def __init__(self):
        self.body = ""
        # move to abstract
        #self.endian
        #self.formater
        #self.endline

    def generate_class(self, struct_dto: struct_dto):
        self.create_file_header(struct_dto.name)

        for variable in struct_dto.variables:
            dart_type = DartVariableType.convert(variable)
            self.body += "\t" + dart_type.name + " " + variable.name + ";\n"

        self.body += "\n\t" + struct_dto.name + "({" + "\n"
        for variable in struct_dto.variables:
            self.body += "\t\t this." + variable.name + ",\n"
        self.body += "\t});" + "\n"

        self.body += "}"

        print(self.body)

    def generate_parse_function(self, struct_dto):
        pass

    def create_file_header(self, struct_name):
        self.body = "class " + struct_name + " {" + "\n"
