'''
Problem link: https://leetcode.com/problems/3sum-closest/
Difficulty: Medium
Approach: use 2 pointer technique fixing i, update j and k in O(n)
T.C: O(n**2)
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l = len(nums)
        min_val = float('inf')
        nums.sort()
        for i in range(l-2):
            j, k = i+1, l-1
            while j<k:
                sm = nums[i]+nums[j]+nums[k]

                if abs(sm-target) < abs(min_val):
                    min_val = sm-target
                    ans = sm

                if sm < target:
                    j+=1
                else:
                    k-=1

                if min_val == 0:
                    break
        print(ans)
        return ans
            
            
        