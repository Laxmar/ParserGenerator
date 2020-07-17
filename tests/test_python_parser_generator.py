import unittest

from src.struct_dto import StructDto
from src.variable_dto import VariableDto


class TestStructDto(unittest.TestCase):

    def setUp(self):
        pass

    def test_extract_line_with_tabs(self):
        struct_dto = StructDto()
        struct_dto.name = "TestStruct"
        var1 = VariableDto("uint8_t", "param1")
        var2 = VariableDto("uint16_t", "param2")
        var3 = VariableDto("uint16_t", "param3")
        struct_dto.variables.append(var1)
        struct_dto.variables.append(var2)
        struct_dto.variables.append(var3)


