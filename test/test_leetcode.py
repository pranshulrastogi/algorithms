from unittest import result
from datastructures import linkedlist
from leetcode import (
    nth_tribonacci_number,
    climbing_stairs,
    find_all_duplicates_in_an_array,
    house_robber,
    delete_and_earn,
    house_robber_ii,
    word_search_ii,
    break_a_palindrome,
    guess_number_higher_or_lower,
    best_time_to_buy_and_sell_stock_with_cooldown,
    best_time_to_buy_and_sell_stock_iii,
    reverse_words_in_a_string,
    sort_characters_by_frequency,
    jump_game,
    arranging_coins,
    unique_binary_search_trees,
    minimum_value_to_get_positive_step_by_step_sum,
    remove_linked_list_elements,
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

    def test_word_search_ii(self):
        input_output = [
            (
                [
                    [
                        ["o", "a", "a", "n"],
                        ["e", "t", "a", "e"],
                        ["i", "h", "k", "r"],
                        ["i", "f", "l", "v"],
                    ],
                    ["oath", "pea", "eat", "rain"],
                ],
                ["eat", "oath"],
            ),
            ([[["a", "a"]], ["aaa"]], []),
        ]
        for input, output in input_output:
            result = word_search_ii.findWords(input[0], input[1])
            self.assertCountEqual(result, output)

    def test_break_a_palindrome(self):
        input_output = [("abccba", "aaccba"), ("a", ""), ("aa", "ab"), ("aba", "abb")]
        for input, output in input_output:
            result = break_a_palindrome.breakPalindrome(input)
            self.assertEqual(output, result)

    def test_guess_number_higher_or_lower(self):
        input_output = [
            ([10, 6], 6),
            ([1, 1], 1),
            ([2, 1], 1),
            ([2, 2], 2),
            ([500, 499], 499),
            ([5, 5], 5),
            ([1, 0], 0),
        ]
        for input_list, output in input_output:
            input, pick = input_list
            guess_number_higher_or_lower.set_pick(pick)
            result = guess_number_higher_or_lower.guessNumber(input)
            self.assertEqual(output, result)

    def test_best_time_to_buy_and_sell_stock_with_cooldown(self):
        input_output = [([1, 2, 3, 0, 2], 3), ([1], 0), ([1, 2], 1)]
        for input, output in input_output:
            result = best_time_to_buy_and_sell_stock_with_cooldown.maxProfit(input)
            self.assertEqual(output, result)

    def test_best_time_to_buy_and_sell_stock_iii(self):
        input_output = [
            ([3, 3, 5, 0, 0, 3, 1, 4], 6),
            ([1, 2, 3, 4, 5], 4),
            ([7, 6, 4, 3, 1], 0),
        ]
        for input, output in input_output:
            result = best_time_to_buy_and_sell_stock_iii.maxProfit(input)
            self.assertEqual(result, output)

    def test_reverse_words_in_a_string(self):
        input_output = [
            ("the sky is blue", "blue is sky the"),
            (" hello world ", "world hello"),
            (" Bob    Loves Alice ", "Alice Loves Bob"),
        ]
        for input, output in input_output:
            result = reverse_words_in_a_string.reverseWords(input)
            self.assertEqual(result, output)

    def test_sort_characters_by_frequency(self):
        input_output = [
            ("tree", ["eert", "eetr"]),
            ("cccaaa", ["aaaccc", "cccaaa"]),
            ("Aabb", ["bbAa", "bbaA"]),
        ]
        for input, output in input_output:
            result = sort_characters_by_frequency.frequencySort(input)
            self.assertIn(result, output)

    def test_jump_game(self):
        input_output = [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False)]
        for input, output in input_output:
            result = jump_game.canJump(input)
            self.assertEqual(result, output)

    def test_arranging_coins(self):
        input_output = [(5, 2), (2, 1), (3, 2), (8, 3), (0, 0)]
        for input, output in input_output:
            result = arranging_coins.arrangeCoins(input)
            self.assertEqual(result, output)

    def test_unique_binary_search_trees(self):
        input_output = [(1, 1), (3, 5), (4, 14), (19, 1767263190)]
        for input, output in input_output:
            result = unique_binary_search_trees.numTrees(input)
            self.assertEqual(result, output)

    def test_minimum_value_to_get_positive_step_by_step_sum(self):
        input_output = [([-3, 2, -3, 4, 2], 5), ([1, 2], 1), ([1, -2, -3], 5)]
        for input, output in input_output:
            result = minimum_value_to_get_positive_step_by_step_sum.minStartValue(input)
            self.assertEqual(result, output)

    def test_remove_linked_list_elements(self):
        input_output = [
            (([1, 2, 6, 3, 4, 5, 6], 6), [1, 2, 3, 4, 5]),
            (([], 1), []),
            (([7, 7, 7, 7], 7), []),
        ]
        for input, output in input_output:
            lst, val = input[0], input[1]
            # create a linked list
            ll = linkedlist.LinkedList(lst)
            result = remove_linked_list_elements.removeElements(ll.head, val)
            output_ll = linkedlist.LinkedList(result, from_other_list=True)
            print(output_ll.tolist(), output)
            # self.assertEqual(output_ll.tolist(), output)
