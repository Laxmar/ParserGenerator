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
            VariableType.uint8: DartVariableType.int.name,
            VariableType.uint16: DartVariableType.int.name,
            VariableType.uint32: DartVariableType.int.name,

            VariableType.int8: DartVariableType.int.name,
            VariableType.int16: DartVariableType.int.name,
            VariableType.int32: DartVariableType.int.name,

            VariableType.float: DartVariableType.double.name,
            VariableType.double: DartVariableType.double.name,
            VariableType.bool: DartVariableType.bool.name
        }
        return switcher.get(variable.type, variable.original_type)


class DartParserGenerator(AbstractParserGenerator):

    def __init__(self, endian: Endian):
        super().__init__(endian)
        self.body = ""
        self.input_variable_name = "buffer"
        self.offset_variable_name = "offset"
        self.init_offset_variable_name = "initOffset"
        self.class_variable_name = "result"
        self.variable_size_variable_name = "variable_size"

    def generate_class(self, struct_dto: Struct):
        # TODO add imports
        # import 'dart:typed_data';
        # bool intToBool(int a) => a == 0 ? false : true;

        self.body = "class " + struct_dto.name + " {" + self.end_of_line

        for variable in struct_dto.variables:
            dart_type = DartVariableType.convert(variable)
            self.body += "\t" + dart_type + " " + variable.name + ";" + self.end_of_line
        self.body += self.end_of_line

        self.body += "\t" + struct_dto.name + "({" + self.end_of_line
        for variable in struct_dto.variables:
            self.body += "\t\t this." + variable.name + "," + self.end_of_line
        self.body += "\t});" + self.end_of_line

        self.body += "}"

    def generate_parse_function(self, struct_dto):
        self.body += self.end_of_line
        self.body += "int Parse" + struct_dto.name + "(ByteData " + self.input_variable_name + ", int " + self.init_offset_variable_name + ", " + struct_dto.name + " " + self.class_variable_name + ") {" + self.end_of_line

        self.body += "\t" + "int " + self.offset_variable_name + " = " + self.init_offset_variable_name + ";" + self.end_of_line
        self.body += "\t" + "int " + self.variable_size_variable_name + " = 0;" + self.end_of_line

        for variable in struct_dto.variables:
            self.body += self.end_of_line

            if variable.type is not VariableType.custom:
                self.body += "\t" + self.variable_size_variable_name + " = " + str(variable.size) + ";" + self.end_of_line
                self.body += "\t" + self.class_variable_name + "." + variable.name + " = " + self.__get_parse_function(variable.type) + ";" + self.end_of_line
            else:
                self.body += "\t" + "var " + variable.name + " = new " + variable.original_type + "();" + self.end_of_line
                self.body += "\t" + self.variable_size_variable_name + " = " + "Parse" + variable.original_type + "(" + self.input_variable_name + ", " + self.offset_variable_name + ", " + variable.name + ");" + self.end_of_line

            self.body += "\t" + self.offset_variable_name + " += " + self.variable_size_variable_name + ";" + self.end_of_line

        self.body += self.end_of_line
        self.body += "\t" + "return " + self.offset_variable_name + ";" + self.end_of_line
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
            VariableType.bool:  "getUint8"
        }
        function_name = switcher.get(variable_type)

        endian_param = ""
        if variable_type is not VariableType.uint8 and variable_type is not VariableType.int8 and variable_type is not VariableType.bool:
            if self.endian == Endian.LITTLE:
                endian_param = ", Endian.little"
            else:
                endian_param = ", Endian.big"

        function_str = self.input_variable_name + "." + function_name + "(" + self.offset_variable_name + endian_param + ")"

        # TODO refactor
        if variable_type == VariableType.bool:
            return "intToBool(" + function_str + ")"
        else:
            return function_str
