import unittest

from src.struct_dto import StructDto
from src.variable_dto import VariableDto


class TestStructDto(unittest.TestCase):

    def setUp(self):
        pass

    def test_extract_line_with_tabs(self):
        struct_dto = StructDto()
        line = "\t\tuint8_t param\t"
        struct_dto.extract_variable_from_line(line)

        variable: VariableDto = struct_dto.variables[0]
        self.assertEqual(variable.name, "param")
        self.assertEqual(variable.type, "uint8_t")

    def test_extract_line_with_extra_newline(self):
        struct_dto = StructDto()
        line = "\t\tuint8_t param;\n"
        struct_dto.extract_variable_from_line(line)

        variable: VariableDto = struct_dto.variables[0]
        self.assertEqual(variable.name, "param")
        self.assertEqual(variable.type, "uint8_t")

    def test_extract_line_with_spaces(self):
        struct_dto = StructDto()
        line = "\t\t uint8_t param; \n"
        struct_dto.extract_variable_from_line(line)

        variable: VariableDto = struct_dto.variables[0]
        self.assertEqual(variable.name, "param")
        self.assertEqual(variable.type, "uint8_t")


if __name__ == '__main__':
    unittest.main()