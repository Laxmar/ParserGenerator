import re

from src.struct import Struct


# TODO handle nested struct
# TODO handle unions
def extract_struct_from_file(file_path):
    is_struct_started = False
    struct_dtos = []
    struct_dto = Struct()

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:

            if line.find("struct") != -1:
                struct_dto = Struct()
                is_struct_started = True
                struct_dto.name = line.split(" ")[1]
                continue
            if line.find("}") != -1 and is_struct_started:
                is_struct_started = False
                struct_dtos.append(struct_dto)

            if not is_struct_started:
                continue

            if is_struct_started:
                struct_dto.extract_variable_from_line(line)

    return struct_dtos
