import re

from src.variable_dto import VariableDto


class StructDto:

    def __init__(self):
        self.name = ""
        self.variables = []

    def __str__(self):
        return self.name + "\n" + " ".join([str(var) for var in self.variables])

    def extract_variable_from_line(self, line):
        tokens = re.findall(r"[\w']+", line)

        # TODO raise wrong format exception
        if len(tokens) > 2:
            raise Exception()

        variable_dto = VariableDto(tokens[0], tokens[1])
        self.variables.append(variable_dto)