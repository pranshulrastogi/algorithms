'''
Problem Link: https://leetcode.com/problems/reduce-array-size-to-the-half/
Difficulty: Medium
'''

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        from sortedcontainers import SortedList
        count_d = collections.Counter(arr) # get the count of every integer in arr O(n)
        counts = SortedList() # to maintain the sorted list of counts
        
        for k,v in count_d.items():
            counts.add(v)
        counts = counts[::-1]    # we want descending order, O(n)
        n = len(arr)
        x= n
        i=0
        ans = 0
        # the best way is to remove max occuring elements first, this way 
        # we can minimize the set size
        while x > n//2 and i<len(counts):
            ans+=1
            x -= counts[i]
            i+=1
        print(ans)
        return ans