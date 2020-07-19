from enum import Enum


class Endian(Enum):
    LITTLE = "little"
    BIG = "big"

    @staticmethod
    def get_names() -> [str]:
        return [name.lower() for name, member in Endian.__members__.items()]

    @staticmethod
    def is_supported(endian: str) -> bool:
        return endian.lower() in Endian.get_names()

    @staticmethod
    def get_from_name(input_name: str):
        return {name.lower(): member for name, member in Endian.__members__.items()}.get(input_name.lower())