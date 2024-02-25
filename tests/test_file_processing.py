import sys
import unittest

sys.path.append("..")


from file_processing import (
    get_byte_count,
    get_character_count,
    get_line_count,
    get_word_count,
    process_file,
)


class TestProcessFile(unittest.TestCase):
    def test_process_file(self):
        def double(x):
            return {"answer": x * 2}

        results = process_file(2, [double])
        self.assertEqual(results, {"answer": 4})


class TestGetByteCount(unittest.TestCase):
    def test_no_bytes(self):
        test_data = ""
        test_data_file_object = test_data.encode()

        byte_count_object = get_byte_count(test_data_file_object)
        self.assertEqual(byte_count_object["bytes"], 0)

    def test_one_byte(self):
        test_data = "\n"
        test_data_file_object = test_data.encode()

        byte_count_object = get_byte_count(test_data_file_object)
        self.assertEqual(byte_count_object["bytes"], 1)

    def test_three_bytes(self):
        test_data = "AB\n"
        test_data_file_object = test_data.encode()

        byte_count_object = get_byte_count(test_data_file_object)
        self.assertEqual(byte_count_object["bytes"], 3)


class TestGetLineCount(unittest.TestCase):
    def test_no_lines(self):
        test_data = ""
        test_data_file_object = test_data.encode()

        line_count_object = get_line_count(test_data_file_object)
        self.assertEqual(line_count_object["lines"], 0)

    def test_one_line(self):
        test_data = "This is a test line\n"
        test_data_file_object = test_data.encode()

        line_count_object = get_line_count(test_data_file_object)
        self.assertEqual(line_count_object["lines"], 1)

    def test_three_lines(self):
        test_data = "This is a test line\nAnd another line\nAnd a third\n"
        test_data_file_object = test_data.encode()

        line_count_object = get_line_count(test_data_file_object)
        self.assertEqual(line_count_object["lines"], 3)


class TestGetWordCount(unittest.TestCase):
    def test_no_words(self):
        test_data = ""
        test_data_file_object = test_data.encode()

        word_count_object = get_word_count(test_data_file_object)
        self.assertEqual(word_count_object["words"], 0)

    def test_one_word(self):
        test_data = "word\n"
        test_data_file_object = test_data.encode()

        word_count_object = get_word_count(test_data_file_object)
        self.assertEqual(word_count_object["words"], 1)

    def test_three_words(self):
        test_data = "Test three words\n"
        test_data_file_object = test_data.encode()

        word_count_object = get_word_count(test_data_file_object)
        self.assertEqual(word_count_object["words"], 3)

    def test_10_words_over_three_lines(self):
        test_data = "Test three words\nOver three lines\nIt should definitely work\n"
        test_data_file_object = test_data.encode()

        word_count_object = get_word_count(test_data_file_object)
        self.assertEqual(word_count_object["words"], 10)


class TestGetCharacterCount(unittest.TestCase):
    def test_no_characters(self):
        test_data = ""
        test_data_file_object = test_data.encode()

        character_count_object = get_character_count(test_data_file_object)
        self.assertEqual(character_count_object["characters"], 0)

    def test_one_character(self):
        test_data = "\n"
        test_data_file_object = test_data.encode()

        character_count_object = get_character_count(test_data_file_object)
        self.assertEqual(character_count_object["characters"], 1)

    def test_three_characters(self):
        test_data = "AB\n"
        test_data_file_object = test_data.encode()

        character_count_object = get_character_count(test_data_file_object)
        self.assertEqual(character_count_object["characters"], 3)


if __name__ == "__main__":
    unittest.main()
