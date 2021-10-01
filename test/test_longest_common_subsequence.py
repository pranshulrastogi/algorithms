import unittest
from leetcode import longest_common_subsequence as lcs


class TestLCS(unittest.TestCase):
    def test_longestCommonSubsequence(self):
        text1 = "abcde"
        text2 = "ace"
        output = lcs.longestCommonSubsequence(text1, text2)
        self.assertEqual(output, 3)
