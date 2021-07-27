'''
Problem link: https://leetcode.com/problems/isomorphic-strings/
Difficulty: Easy
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sn = [] # encoding of characters in s(we use label encoding, i.e. for every new character we add integer)
        tn = []
        d = {}
        i=0
        for c in s:
            if d.get(c,None) is not None:
                sn.append(d[c])
            else:
                d[c] = i
                i+=1
                sn.append(d[c])
        i=0
        d = {}
        for c in t:
            if d.get(c,None) is None:
                d[c] = i
                i+=1
            tn.append(d[c])
        print(sn,tn)
        return sn==tn