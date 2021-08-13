'''
Problem Link: https://leetcode.com/problems/subsets-ii/
Difficulty : Medium
Catch: output should not contain duplicates
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from sortedcontainers import SortedList # we are using SortedList inorder to identify duplicates
        l = len(nums)
        ans = []
        def getsubsets(nums,i,l, subset):
            if i==l:
                ans.append(subset)
                # print("adding ", subset)
                return
            else:
                # one option is to take it
                getsubsets(nums, i+1, l, subset+(nums[i],))
                # another is to leave it
                getsubsets(nums, i+1, l, subset)
        getsubsets(nums, 0, l, SortedList())
        # make elements hashable in-order to convert it to set
        # to remove the duplicates
        ans = [tuple(ele) for ele in ans]
        ans = set(ans)
        
        return ans