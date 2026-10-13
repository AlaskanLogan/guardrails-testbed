import unittest

from strutil import reverse_words


class TestReverseWords(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(reverse_words("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_many_words(self):
        self.assertEqual(reverse_words("the quick brown fox"), "fox brown quick the")

    def test_extra_whitespace(self):
        self.assertEqual(reverse_words("  a   b  c "), "c b a")

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_only_whitespace(self):
        self.assertEqual(reverse_words("   "), "")


if __name__ == "__main__":
    unittest.main()
