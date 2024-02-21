import argparse
import os


def file_exists(filename):
    if not os.path.exists(filename):
        return False
    return True


def print_byte_count(filename):
    byte_count = os.path.getsize(filename)
    print(byte_count, filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ccwc",
        description="Finds the number of bytes, words, characters, and multibyte characters in a text file",
    )

    parser.add_argument("-c", help="count the number of bytes", action="store_true")
    parser.add_argument("filename", help="the filename to be checked")
    args = parser.parse_args()

    if not file_exists(args.filename):
        raise argparse.ArgumentTypeError(f"The file {args.filename} does not exist.")

    if args.c:
        byte_count = print_byte_count(args.filename)
