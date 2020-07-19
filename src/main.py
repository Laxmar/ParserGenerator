from src import abstract_parser_generator
from src.endian import Endian
from src.file_analyzer import extract_struct_from_file
from src.parser_generator_factory import ParserGeneratorFactory, Language

if __name__ == '__main__':
    print("Starting program")

    # TODO read args
    language_input = "dart"
    endian_input = "little"

    # TODO if --help print help:
    # print_help()
    # TODO validate inputs
    # Language.is_supported(language_input)
    # Endian.is_supported(endian_input)

    # TODO convert inputs
    # file_path = "../tests/files/SimplestStuct.h"
    file_path = "../tests/files/TwoStructs.h"
    language = Language.get_from_name(language_input)
    endian = Endian.get_from_name(endian_input)
    #name_format

    structs = extract_struct_from_file(file_path)
    for struct in structs:
        print(struct)

    parser_generator: abstract_parser_generator = ParserGeneratorFactory.create(language, endian)

    parser_generator.generate_class(structs[0])
    # parser_file = parserGenerator.generate(structs)
    # extension = get_file_extension(language)
    # file_name = create_file_name(sth, extension)
    # save_to_file(parser_file, file_name)


def print_help():
    # print("Available language:")
    # languages = Language.get_names()
    # for l in languages:
    #     print("- " + l)
    pass