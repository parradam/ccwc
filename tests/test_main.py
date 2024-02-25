import subprocess
import sys
import unittest

sys.path.append("..")


class TestMainFile(unittest.TestCase):
    def test_default(self):
        result = subprocess.run(
            ["python", "main.py", "tests/test_file.txt"], capture_output=True
        )
        self.assertEqual(result.stdout, b"3\t3\t13\ttests/test_file.txt\n")

    def test_byte_flag(self):
        result = subprocess.run(
            ["python", "main.py", "-c", "tests/test_file.txt"], capture_output=True
        )
        self.assertEqual(result.stdout, b"13\ttests/test_file.txt\n")

    def test_line_flag(self):
        result = subprocess.run(
            ["python", "main.py", "-l", "tests/test_file.txt"], capture_output=True
        )
        self.assertEqual(result.stdout, b"3\ttests/test_file.txt\n")

    def test_word_flag(self):
        result = subprocess.run(
            ["python", "main.py", "-w", "tests/test_file.txt"], capture_output=True
        )
        self.assertEqual(result.stdout, b"3\ttests/test_file.txt\n")

    def test_character_flag(self):
        result = subprocess.run(
            ["python", "main.py", "-m", "tests/test_file.txt"], capture_output=True
        )
        self.assertEqual(result.stdout, b"13\ttests/test_file.txt\n")

    def test_pipe_default(self):
        input_data = b"test\nthe\npipe\n\n"
        result = subprocess.run(
            ["python", "main.py"], input=input_data, capture_output=True
        )
        self.assertEqual(result.stdout, b"4\t3\t15\n")

    def test_pipe_byte_flag(self):
        input_data = b"test\nthe\npipe\n\n"
        result = subprocess.run(
            ["python", "main.py", "-c"], input=input_data, capture_output=True
        )
        self.assertEqual(result.stdout, b"15\n")

    def test_pipe_line_flag(self):
        input_data = b"test\nthe\npipe\n\n"
        result = subprocess.run(
            ["python", "main.py", "-l"], input=input_data, capture_output=True
        )
        self.assertEqual(result.stdout, b"4\n")

    def test_pipe_word_flag(self):
        input_data = b"test\nthe\npipe\n\n"
        result = subprocess.run(
            ["python", "main.py", "-w"], input=input_data, capture_output=True
        )
        self.assertEqual(result.stdout, b"3\n")

    def test_pipe_character_flag(self):
        input_data = b"test\nthe\npipe\n\n"
        result = subprocess.run(
            ["python", "main.py", "-m"], input=input_data, capture_output=True
        )
        self.assertEqual(result.stdout, b"15\n")
