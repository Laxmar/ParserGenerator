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


class VariableDto:
    def __init__(self, type_str: str, name: str):
        self.type = self.map_variable_type(type_str)
        self.name = name
        # size in bits or byte
        # self.size = get_size()

    def __str__(self):
        return "VariableDto name=" + self.name + " type=" + str(self.type.name)

    @staticmethod
    def map_variable_type(variable_type):
        # TODO add support for short, int, etc.
        switcher = {
            "uint8_t": VariableType.uint8,
            "int8_t": VariableType.int8,
            "uint16_t": VariableType.uint16,
            "int16_t": VariableType.int16,
            "uint32_t": VariableType.uint32,
            "int32_t": VariableType.int32,
            "float": VariableType.float,
            "double": VariableType.double,
            "bool": VariableType.bool
        }
        # TODO should return custom or type?
        return switcher.get(variable_type, VariableType.custom)
