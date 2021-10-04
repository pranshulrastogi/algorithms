from leetcode import jump_game
import unittest


class TestJumpGame(unittest.TestCase):
    def test_jump_game(self):
        input_output = [
            ([2, 3, 1, 1, 4], True),
            ([3, 2, 1, 0, 4], False),
            ([0, 2, 3], False),
            ([1, 1], True),
            ([0, 1], False),
            ([0], True),
        ]
        for input, output in input_output:
            self.assertEqual(jump_game.canJump(input), output)
