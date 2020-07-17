from enum import Enum


class Language(Enum):
    PYTHON = "python",
    DART = "dart"

    @staticmethod
    def get_names() -> [str]:
        return [name.lower() for name, member in Language.__members__.items()]

    @staticmethod
    def is_supported(language: str) -> bool:
        return language.lower() in Language.get_names()

    @staticmethod
    def get_from_name(input_name: str):
        return {name.lower(): member for name, member in Language.__members__.items()}.get(input_name.lower())
