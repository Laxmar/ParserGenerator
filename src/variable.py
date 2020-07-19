from enum import Enum


class VariableType(Enum):
    uint8 = "uint8",
    int8 = "int8"

    uint16 = "uint16"
    int16 = "int16"

    uint32 = "uint32"
    int32 = "int32"

    float = "float"
    double = "double"
    bool = "bool"

    custom = "custom"


class Variable:
    def __init__(self, type_str: str, name: str):
        self.original_type = type_str
        self.__map_variable_type(type_str)
        self.name = name

    def __str__(self):
        return "VariableDto name=" + self.name + " type=" + str(self.type.name)

    def __map_variable_type(self, variable_type):
        # TODO add support for short, int, etc.
        switcher = {
            "uint8_t": (VariableType.uint8, 1),
            "int8_t": (VariableType.int8, 1),
            "uint16_t": (VariableType.uint16, 2),
            "int16_t": (VariableType.int16, 2),
            "uint32_t": (VariableType.uint32, 4),
            "int32_t": (VariableType.int32, 4),
            "float": (VariableType.float, 4),
            "double": (VariableType.double, 4),
            "bool": (VariableType.bool, 1)
        }
        self.type, self.size = switcher.get(variable_type, (VariableType.custom, None))
