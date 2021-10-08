from unittest import result
from leetcode import (
    nth_tribonacci_number,
    climbing_stairs,
    find_all_duplicates_in_an_array,
    house_robber,
    delete_and_earn,
    house_robber_ii,
)
import unittest


class TestLeetcode(unittest.TestCase):
    def test_nth_tribonacci_number(self):
        input_output = [(0, 0), (4, 4), (25, 1389537)]
        for input, output in input_output:
            result = nth_tribonacci_number.tribonacci(input)
            self.assertEqual(result, output)

    def test_climbing_stairs(self):
        input_output = [(1, 1), (2, 2), (3, 3), (4, 5), (45, 1836311903)]
        for input, output in input_output:
            result = climbing_stairs.climbStairs(input)
            self.assertEqual(result, output)

    def test_find_all_duplicates_in_an_array(self):
        input_output = [([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]), ([1, 1, 2], [1]), ([1], [])]
        for input, output in input_output:
            result = find_all_duplicates_in_an_array.findDuplicates(input)
            self.assertEqual(output, result)

    def test_house_robber(self):
        input_output = [([1, 2, 3, 1], 4), ([2, 7, 9, 3, 1], 12), ([5], 5)]
        for input, output in input_output:
            result = house_robber.rob(input)
            self.assertEqual(result, output)

    def test_delete_and_earn(self):
        input_output = [
            ([3, 4, 2], 6),
            ([2, 2, 3, 3, 3, 4], 9),
            ([1, 1, 1, 2, 4, 5, 5, 5, 6], 18),
        ]
        for input, output in input_output:
            result = delete_and_earn.deleteAndEarn(input)
            self.assertEqual(result, output)

    def test_house_robber_ii(self):
        input_output = [([2, 3, 2], 3), ([1, 2, 3, 1], 4), ([1, 2, 3], 3), ([1], 1)]
        for input, output in input_output:
            result = house_robber_ii.rob(input)
            self.assertEqual(result, output)
