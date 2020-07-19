from enum import Enum

from src.abstract_parser_generator import AbstractParserGenerator
from src.endian import Endian
from src.struct import Struct
from src.variable import VariableType, Variable


class DartVariableType(Enum):
    int = "int"
    double = "double"
    bool = "bool"

    # TODO move to Generator
    @staticmethod
    def convert(variable: Variable):
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

    def __init__(self, endian: Endian):
        super().__init__(endian)
        self.body = ""
        self.input_variable_name = "buffer"
        self.offset_variable_name = "offset"
        self.class_variable_name = "result"

    def generate_class(self, struct_dto: Struct):
        self.body = "class " + struct_dto.name + " {" + self.end_of_line

        for variable in struct_dto.variables:
            dart_type = DartVariableType.convert(variable)
            self.body += "\t" + dart_type.name + " " + variable.name + ";" + self.end_of_line
        self.body += self.end_of_line

        self.body += "\t" + struct_dto.name + "({" + self.end_of_line
        for variable in struct_dto.variables:
            self.body += "\t\t this." + variable.name + "," + self.end_of_line
        self.body += "\t});" + self.end_of_line

        # TODO add empty constructor

        self.body += "}"

        # TODO remove print
        print(self.body)

    def generate_parse_function(self, struct_dto):
        # TODO remove magic variables names using self and refactor
        self.body += "int Parse" + struct_dto.name + "(ByteData buffer, int initOffset) {" + self.end_of_line

        self.body += "\t" + "var " + self.class_variable_name + " = new " + struct_dto.name + "();" + self.end_of_line
        self.body += "\t" + "int offset = initOffset;" + self.end_of_line
        self.body += "\t" + "int variableSize = 0" + self.end_of_line

        for variable in struct_dto.variables:

            if variable.type is not VariableType.custom:
                self.body += "\t" + "variableSize = " + str(variable.size) + ";" + self.end_of_line
                self.body += "\t" + self.class_variable_name + "." + variable.name + " = " + self.__get_parse_function(variable.type) + ";" + self.end_of_line
            else:
                self.body += "\t" + "var " + variable.original_type + " = new " + variable.original_type + "();" + self.end_of_line
                self.body += "\t" + "variableSize = " + "Parse" + variable.original_type + "(buffer, offset);" + self.end_of_line

            self.body += "\t" + "offset += variableSize;" + self.end_of_line

        self.body += "}" + self.end_of_line

        # TODO remove print
        print(self.body)

    def __get_parse_function(self, variable_type: VariableType) -> str:
        switcher = {
            VariableType.uint8: "getUint8",
            VariableType.uint16: "getUint16",
            VariableType.uint32: "getUint32",

            VariableType.int8: "getInt8",
            VariableType.int16: "getInt16",
            VariableType.int32: "getInt32",

            VariableType.float: "getFloat32",
            VariableType.double: "getFloat64",
            VariableType.bool:  "getUint8"  # TODO add cast? Test this
        }
        function_name = switcher.get(variable_type)

        endian_param = ""
        if variable_type is not VariableType.uint8 and variable_type is not VariableType.int8 and variable_type is not VariableType.bool:
            if self.endian == Endian.LITTLE:
                endian_param = ", Endian.small"
            else:
                endian_param = ", Endian.big"

        return self.input_variable_name + "." + function_name + "(" + self.offset_variable_name + endian_param + ")"
