'''
Problem: https://leetcode.com/problems/intersection-of-two-arrays-ii/
Difficulty: Easy
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        l1, l2 = len(nums1), len(nums2)
        ans = []
        while i<l1 and j<l2:
            if nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
                j+=1
        print(ans)
        return ans
        