'''
Problem: https://leetcode.com/problems/max-consecutive-ones/
Difficulty: Easy
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for ele in nums:
            if ele:
                count+=1
            else:
                ans = max(ans,count)
                count=0
        ans = max(ans,count)
        print(ans)
        return ans
        