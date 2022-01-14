"""
Problem link: https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
Difficulty: Medium
logic hint:
split the given array on 0 as 0 contaminates the array
"""


def getMaxLen(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    def split_on_zero(arr):
        temp = []
        result = []
        for ele in arr:
            if ele == 0 and temp:
                result.append(temp)
                temp = []
            else:
                if ele != 0:
                    temp.append(ele)
        if temp:
            result.append(temp)
            temp = []
        return result

    nums_list = split_on_zero(nums)

    def count_negatives(arr):
        result = 0
        for ele in arr:
            if ele < 0:
                result += 1
        return result

    def find_first_neg(arr, reverse=False):
        if not reverse:

            for i, ele in enumerate(arr, start=0):
                if ele < 0:
                    return i + 1
        else:

            new_arr = arr[::-1]
            for i, ele in enumerate(new_arr, start=0):
                if ele < 0:
                    return i + 1

    # for each of the list, do following:
    # count number of -ves
    # if its %2==0 , ans = full array for that list
    # else: val = min(distance_of_negative_from_left, distance_of_negative_from_right)
    # ans = len(lst) - val

    ans = 0

    for lst in nums_list:
        l = len(lst)
        negatives = count_negatives(lst)
        if negatives % 2 == 0:
            lst_ans = l
        else:
            val = min(find_first_neg(lst), find_first_neg(lst, reverse=True))
            lst_ans = l - val
        ans = max(ans, lst_ans)
    return ans
