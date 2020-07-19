from enum import Enum

from src.abstract_parser_generator import AbstractParserGenerator
from src.endian import Endian
from src.struct import Struct
from src.variable import VariableType, Variable


class DartVariableType(Enum):
    int = "int"
    double = "double"
    bool = "bool"

    @staticmethod
    def convert(variable: Variable):
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
    # TODO pass params for formating implement in AbstractParserGenerator
    def __init__(self, endian: Endian):
        super().__init__(endian)
        self.body = ""
        # self.formater

    def generate_class(self, struct_dto: Struct):
        self.body = "class " + struct_dto.name + " {" + self.end_of_line

        for variable in struct_dto.variables:
            dart_type = DartVariableType.convert(variable)
            self.body += "\t" + dart_type.name + " " + variable.name + self.end_of_line
        self.body += self.end_of_line

        self.body += "\t" + struct_dto.name + "({" + self.end_of_line
        for variable in struct_dto.variables:
            self.body += "\t\t this." + variable.name + "," + self.end_of_line
        self.body += "\t});" + self.end_of_line

        self.body += "}"

        print(self.body)

    def generate_parse_function(self, struct_dto):
        pass
