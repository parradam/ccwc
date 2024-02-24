import argparse
import os
import sys


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


def print_message(filename, results):
    print_order = ["lines", "words", "bytes", "characters"]
    message = []

    for key_to_search in print_order:
        result = results.get(key_to_search, False)

        if result:
            message.append(str(result))

    if filename:
        message.append(filename)

    message_to_print = "\t".join(message)
    print(message_to_print)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ccwc",
        description="Finds the number of bytes, words, characters, and multibyte characters in a text file",
    )

    parser.add_argument(
        "-c", "--byte", help="count the number of bytes", action="store_true"
    )
    parser.add_argument(
        "-l", "--line", help="count the number of lines", action="store_true"
    )
    parser.add_argument(
        "-w", "--word", help="count the number of words", action="store_true"
    )
    parser.add_argument(
        "-m", "--char", help="count the number of characters", action="store_true"
    )
    parser.add_argument("filename", nargs="?", help="the filename to be checked")
    args = parser.parse_args()

    if args.filename and not file_exists(args.filename):
        raise argparse.ArgumentTypeError(f"The file {args.filename} does not exist.")

    if args.filename:
        try:
            with open(args.filename, "rb") as f:
                fileAsBytes = f.read()
        except PermissionError:
            print(f"Incorrect permissions for {args.filename}")
            sys.exit(1)
        except OSError:
            print(f"Could not open {args.filename}")
            sys.exit(1)
    else:
        fileAsBytes = sys.stdin.buffer.read()

    funcs_to_run = []

    if not any([args.byte, args.line, args.word, args.char]):
        funcs_to_run.append(get_line_count)
        funcs_to_run.append(get_word_count)
        funcs_to_run.append(get_byte_count)
    else:
        if args.byte:
            funcs_to_run.append(get_byte_count)
        if args.line:
            funcs_to_run.append(get_line_count)
        if args.word:
            funcs_to_run.append(get_word_count)
        if args.char:
            funcs_to_run.append(get_character_count)

    results = process_file(fileAsBytes, funcs_to_run)
    print_message(args.filename, results)
