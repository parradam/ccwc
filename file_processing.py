import os


def file_exists(filename):
    if os.path.exists(filename):
        return True
    return False


def process_file(fileAsBytes, funcs):
    results_dict = {}
    for func in funcs:
        result = func(fileAsBytes)
        results_dict.update(result)
    return results_dict


def get_byte_count(fileAsBytes):
    byte_count = len(fileAsBytes)
    return {"bytes": byte_count}


def get_line_count(fileAsBytes):
    file_content = fileAsBytes.decode("utf-8")
    line_count = file_content.count("\n")
    return {"lines": line_count}


def get_word_count(fileAsBytes):
    file_content = fileAsBytes.decode("utf-8")
    word_count = 0
    for line in file_content.splitlines():
        words = line.split()
        word_count += len(words)
    return {"words": word_count}


def get_character_count(fileAsBytes):
    file_content = fileAsBytes.decode("utf-8")
    character_count = 0
    for line in file_content:
        character_count += len(line)
    return {"characters": character_count}
