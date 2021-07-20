'''
Problem link: https://leetcode.com/problems/find-peak-element/
Difficulty: Medium
need to do in O(log n) time
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(-2**31-1) # add -infinity to cover corner cases
        n = len(nums)
        def bs(i,j):
            if i<-1 or j<-1 or i>n or j>n:
                return False
            if i>j:
                return False
            else:
                mid = (i+j)//2
                if mid-1 >=-1 and mid+1 <= n and (nums[mid-1] < nums[mid] > nums[mid+1]):
                    return mid
                else:
                    a= bs(i,mid-1)
                    if a or not isinstance(a,bool):
                        return a
                    # print("a didn't do anything, searching b")
                    b = bs(mid+1, j)
                    return b
        ans = bs(0,n-1)
        print(ans)
        return ans