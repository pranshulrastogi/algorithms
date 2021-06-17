'''
Problem link: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
Difficulty:
Problem:
We are given an array nums of positive integers, and two positive integers left and right (left <= right).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least left and at most right.

Example:
Input: 
nums = [2, 1, 4, 3]
left = 2
right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Note:

left, right, and nums[i] will be an integer in the range [0, 109].
The length of nums will be in the range of [1, 50000].

'''

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        l_i=-1
        r_i=-1
        ans = 0
        for i, nm in enumerate(nums):
            if nm >= left:
                l_i = i
            if nm > right:
                r_i = i
            ans += l_i-r_i
        print(ans)
        return ans