from leetcode import nth_tribonacci_number
import unittest


class TestLeetcode(unittest.TestCase):
    def test_nth_tribonacci_number(self):
        input_output = [(0, 0), (4, 4), (25, 1389537)]
        for input, output in input_output:
            result = nth_tribonacci_number.tribonacci(input)
            self.assertEqual(result, output)
