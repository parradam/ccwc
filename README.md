# ccwc

`ccwc` replicates a subset of the functionality of the utility `wc`. This originated from a coding challenge which is available [here](https://codingchallenges.fyi/challenges/challenge-wc/).

Functionality includes counts of:

- Bytes
- Lines
- Words
- Characters

A text stream can also be piped to `stdin` of `ccwc`.

## Getting Started

### Prerequisites

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)

### Setup

#### Cloning the repository

Ensure that Git and Python are installed, then run:

```sh
git clone git@github.com:parradam/ccwc.git
```

#### Installing dependencies

To install dependencies, run:

```sh
pip install requirements.txt
```

#### Verifying installation

Navigate to the root of the repository, then run:

```sh
python main.py .gitignore
```

This should yield `4       5       45      .gitignore`.

### Running ccwc

Running `python main.py -h` yields:

```text
positional arguments:
  filename    the filename to be checked

optional arguments:
  -h, --help  show this help message and exit
  -c, --byte  count the number of bytes
  -l, --line  count the number of lines
  -w, --word  count the number of words
  -m, --char  count the number of characters
```

#### File examples

##### Default (no optional arguments)

`ccwc` will run the equivalent of `-lwc`, returning the line, word, and byte counts, as well as the filename.

```sh
python main.py test.txt
> 7145    58164   342190  test.txt
```

#### Optional arguments

Any combination of flags can be used, but note that the order will always be as specified in the **Running ccwc** section.

```sh
python main.py -l test.txt
> 7145    test.txt
```

#### Text stream example

A text stream can also be piped to `stdin` of `ccwc`.

Note that no filename is displayed in the output, as the input to `ccwc` was not a file.

```sh
cat test.txt | python main.py
> 7145    58164   342190
```

Optional arguments can also be used.

```sh
cat test.txt | python main.py -l
> 7145
```

## Development

### Running tests

To start the unit tests, run:

```sh
python -m unittest
```

### Checking with mypy

`mypy` is used for type hinting. To check a file, run:

```sh
mypy main.py
```

## Deployment

You may wish to alias this to `ccwc`.

## Authors

- **Adam Parr** - *Provided README Template* -
    [parradam](https://github.com/parradam)

## License

Refer to `LICENSE` for details.

## Acknowledgments

- [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-wc/)
- [PurpleBooth](https://github.com/PurpleBooth) for the original version of the README template
