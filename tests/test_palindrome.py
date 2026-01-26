from unittest import TestCase

from polendrom.palindrome import is_palindrome


class TestPalindrome(TestCase):

    def test_empty_str(self):
        self.assertTrue(is_palindrome(""))

    def test_long1_str(self):
        self.assertTrue(is_palindrome("s"))

    def test_long2_str(self):
        self.assertTrue(is_palindrome("aa"))
        self.assertFalse(is_palindrome("er"))

    def test_long5_str(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("radat"))