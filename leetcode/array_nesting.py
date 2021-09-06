'''
Problem link: https://leetcode.com/problems/array-nesting/
Difficulty: Medium
Trick is to have an array ready for visited nodes, since node that is visited already
is a part of cycle and so are the other ones
'''
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        mcount=0
        n = len(nums)

        visited = [0 for i in range(n)]
        for k in range(n):
            if not visited[k]:
                ele = nums[k]
                count=0
                visited[ele]=1
                while True:
                    ele = nums[ele]
                    count+=1
                    visited[ele]=1
                    if ele==nums[k]:
                        break
                mcount=max(count,mcount)
        print(mcount)
        return mcount
                    
                    