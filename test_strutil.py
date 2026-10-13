import unittest

from strutil import reverse_words


class ReverseWordsTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_single_word(self):
        self.assertEqual(reverse_words("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_multiple_spaces_between_words(self):
        self.assertEqual(reverse_words("a  b   c"), "c b a")

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(reverse_words("  hello world  "), "world hello")

    def test_only_spaces(self):
        self.assertEqual(reverse_words("   "), "")


if __name__ == "__main__":
    unittest.main()
