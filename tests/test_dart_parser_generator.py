import unittest

from src.dart_parser_generator import DartParserGenerator
from src.endian import Endian
from src.struct import Struct
from src.variable import Variable


class TestDartParserGenerator(unittest.TestCase):

    def setUp(self):
        self.struct_dto = Struct()
        self.struct_dto.name = "TestStruct"
        var1 = Variable("uint8_t", "param1")
        var2 = Variable("uint16_t", "param2")
        var3 = Variable("CustomClass", "param3")
        self.struct_dto.variables.append(var1)
        self.struct_dto.variables.append(var2)
        self.struct_dto.variables.append(var3)

    def test_class_generation(self):

        endian = Endian.LITTLE
        generator = DartParserGenerator(endian)
        dart_class = generator.generate_class(self.struct_dto)
        print(dart_class)

    def test_function_generation(self):
        endian = Endian.LITTLE
        generator = DartParserGenerator(endian)
        dart_class = generator.generate_parse_function(self.struct_dto)
        print(dart_class)



