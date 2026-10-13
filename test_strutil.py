import unittest

from strutil import reverse_words


class TestReverseWords(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_single_word(self):
        self.assertEqual(reverse_words("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_many_words(self):
        self.assertEqual(reverse_words("a b c d"), "d c b a")

    def test_extra_whitespace_collapsed(self):
        self.assertEqual(reverse_words("  one   two  three  "), "three two one")

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(reverse_words("  foo bar  "), "bar foo")


if __name__ == "__main__":
    unittest.main()
