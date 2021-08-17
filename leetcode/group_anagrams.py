'''
Problem link: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_strs = ["".join(sorted(s)) for s in strs]
        dct = DefaultDict(list)
        for ix, s in enumerate(sort_strs):
            dct[s].append(ix)
        dct = dict(sorted(dct.items(), key=lambda x: x[0]))
        lst=[]
        ans = []
        for k, indexes in dct.items():
            for ix in indexes:
                lst.append(strs[ix])
            ans.append(lst)
            lst=[]
        return ans
        
        