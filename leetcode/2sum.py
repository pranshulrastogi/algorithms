'''
Problem link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Technique: 2 pointer technique on sorted array
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = DefaultDict(list)
        for ind, ele in enumerate(nums):
            dct[ele].append(ind)
        
        nums.sort()
        i,j=0,len(nums)-1
        while i<j:
            s = nums[i]+nums[j]
            if s == target:
                ans = [dct[nums[i]].pop(0), dct[nums[j]].pop(0)]
                break
            elif s > target:
                j-=1
            else:
                i+=1
        print(ans)
        return ans
        
        