'''
Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Difficulty: medium
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        if l==1:
            return nums[0]
        left, right=0,l-1
        if nums[right] > nums[0]:
            return nums[0] # it is already sorted
        
        while nums[left] > nums[right]:
            mid = (left+right)//2
            if nums[mid] < nums[right]:
                # go left
                right = mid
            else:
                left = mid+1
        ans = nums[left]
        print(ans)
        return ans