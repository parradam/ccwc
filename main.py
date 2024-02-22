import argparse
import os


def file_exists(filename):
    if not os.path.exists(filename):
        return False
    return True


def print_byte_count(filename):
    byte_count = os.path.getsize(filename)
    print(byte_count, filename)


def print_line_count(filename):
    with open(filename, "rb") as f:
        line_count = sum(1 for _ in f)
    print(line_count, filename)


def print_word_count(filename):
    word_count = 0
    with open(filename, "rb") as f:
        for line in f:
            words = line.split()
            word_count += len(words)
    print(word_count, filename)


def print_character_count(filename):
    character_count = 0
    with open(filename, "rb") as f:
        for line in f:
            character_count += len(line.decode())
    print(character_count, filename)


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
        print_byte_count(args.filename)
    if args.l:
        print_line_count(args.filename)
    if args.w:
        print_word_count(args.filename)
    if args.m:
        print_character_count(args.filename)
