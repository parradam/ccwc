import argparse
import os


def file_exists(filename):
    if not os.path.exists(filename):
        return False
    return True


def get_byte_count(filename):
    return os.path.getsize(filename)


def get_line_count(filename):
    with open(filename, "rb") as f:
        line_count = sum(1 for _ in f)
        return line_count


def get_word_count(filename):
    word_count = 0
    with open(filename, "rb") as f:
        for line in f:
            words = line.split()
            word_count += len(words)
    return word_count


def get_character_count(filename):
    character_count = 0
    with open(filename, "rb") as f:
        for line in f:
            character_count += len(line.decode())
    return character_count


def print_message(filename, *args):
    args = [str(arg) for arg in args if arg is not None]
    results = " ".join(args)
    message_to_print = f"{results} {filename}"
    print(message_to_print)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ccwc",
        description="Finds the number of bytes, words, characters, and multibyte characters in a text file",
    )

    parser.add_argument("-c", help="count the number of bytes", action="store_true")
    parser.add_argument("-l", help="count the number of lines", action="store_true")
    parser.add_argument("-w", help="count the number of words", action="store_true")
    parser.add_argument(
        "-m", help="count the number of characters", action="store_true"
    )
    parser.add_argument("filename", help="the filename to be checked")
    args = parser.parse_args()

    if not file_exists(args.filename):
        raise argparse.ArgumentTypeError(f"The file {args.filename} does not exist.")

    if args.c:
        results = [get_byte_count(args.filename)]
    elif args.l:
        results = [get_line_count(args.filename)]
    elif args.w:
        results = [get_word_count(args.filename)]
    elif args.m:
        results = [get_character_count(args.filename)]
    else:
        results = [
            get_byte_count(args.filename),
            get_line_count(args.filename),
            get_word_count(args.filename),
        ]

    print_message(args.filename, *results)
