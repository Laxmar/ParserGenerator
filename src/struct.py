import re

from src.variable import Variable


class Struct:

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

        variable_dto = Variable(tokens[0], tokens[1])
        self.variables.append(variable_dto)