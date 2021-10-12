"""
Problem link: https://leetcode.com/problems/guess-number-higher-or-lower/
Difficulty: Easy
# NOTE
need to define helper function "guess" -> guess(num) which returns 
0 -> when num is the correct number I have in mind(pick)
-1 -> when num is greater than what I have in mind(pick)
1 -> when num is lesser than what I have in mind (pick)
"""


def set_pick(val):
    global _PICK
    _PICK = val


def guess(num):
    """
    @params
    pick -> default value is PICK, need to be given in input before
    starting the test
    """
    if num < _PICK:
        return 1
    elif num > _PICK:
        return -1
    else:
        return 0


def guessNumber(n: int) -> int:
    if n == 1:
        if guess(1) == 0:
            return 1

    def bs(p, q):
        if p == q:
            if guess(p) == 0:
                return p
            else:
                return 0

        my_guess = (p + q) // 2
        direction = guess(my_guess)
        if direction == 0:
            return my_guess
        elif direction == -1:
            return bs(p, my_guess - 1)
        else:
            return bs(my_guess + 1, q)

    ans = bs(1, n)
    return ans
