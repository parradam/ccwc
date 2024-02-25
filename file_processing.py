import os
from typing import Callable, Iterable


def file_exists(filename: str) -> bool:
    return os.path.exists(filename)


def process_file(fileAsBytes: bytes, funcs: Iterable[Callable[[bytes], dict]]) -> dict:
    results_dict = {}
    for func in funcs:
        result = func(fileAsBytes)
        results_dict.update(result)
    return results_dict


def get_byte_count(fileAsBytes: bytes) -> dict:
    byte_count: int = len(fileAsBytes)
    return {"bytes": byte_count}


def get_line_count(fileAsBytes: bytes) -> dict:
    file_content: str = fileAsBytes.decode("utf-8")
    line_count: int = file_content.count("\n")
    return {"lines": line_count}


def get_word_count(fileAsBytes: bytes) -> dict:
    file_content: str = fileAsBytes.decode("utf-8")
    word_count: int = 0
    for line in file_content.splitlines():
        words = line.split()
        word_count += len(words)
    return {"words": word_count}


def get_character_count(fileAsBytes: bytes) -> dict:
    file_content: str = fileAsBytes.decode("utf-8")
    character_count: int = 0
    for line in file_content:
        character_count += len(line)
    return {"characters": character_count}
