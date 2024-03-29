import unittest

from src.struct import Struct
from src.variable import Variable, VariableType


class TestStructDto(unittest.TestCase):

    def setUp(self):
        pass

    def test_extract_line_with_tabs(self):
        struct_dto = Struct()
        line = "\t\tuint8_t param\t"
        struct_dto.extract_variable_from_line(line)

        variable: Variable = struct_dto.variables[0]
        self.assertEqual(variable.name, "param")
        self.assertEqual(variable.type, VariableType.uint8)

    def test_extract_line_with_extra_newline(self):
        struct_dto = Struct()
        line = "\t\tuint8_t param;\n"
        struct_dto.extract_variable_from_line(line)

        variable: Variable = struct_dto.variables[0]
        self.assertEqual(variable.name, "param")
        self.assertEqual(variable.type, VariableType.uint8)

    def test_extract_line_with_spaces(self):
        struct_dto = Struct()
        line = "\t\t uint8_t param; \n"
        struct_dto.extract_variable_from_line(line)

        variable: Variable = struct_dto.variables[0]
        self.assertEqual(variable.name, "param")
        self.assertEqual(variable.type, VariableType.uint8)


if __name__ == '__main__':
    unittest.main()