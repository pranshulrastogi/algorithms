'''
Problem link: https://leetcode.com/problems/array-of-doubled-pairs/
Difficulty: Medium
'''
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        from collections import Counter
        count = Counter(arr)
        for x in sorted(arr, key=abs):
            if count[x]!=0:
                if count[2*x]==0:
                    return False
                count[x] -= 1
                count[2*x] -= 1
        return True
            
        