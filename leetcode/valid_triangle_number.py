'''
Problem link: https://leetcode.com/problems/valid-triangle-number/
Difficulty: Medium
Comment:
submission expect <= O(n**2), so better 2 sort the nums
and then rely on only one property a+b>c, then it becomes 
a sliding window problem, here we first fix the greatest number
as c, and move towards lesser value
'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count=0
        
        l = len(nums)
        nums.sort()
        for c_index in range(l-1,1,-1):
            c = nums[c_index]
            a_index, b_index = 0, c_index-1
            
            while b_index > a_index:
                a, b = nums[a_index], nums[b_index]
                if a+b > c:
                    count += b_index-a_index
                    b_index-=1
                else:
                    a_index+=1
        print(count)
        return count