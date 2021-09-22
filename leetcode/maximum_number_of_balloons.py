'''
Problem: https://leetcode.com/problems/maximum-number-of-balloons/
Difficulty: Easy
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        counter = Counter(text)
        for k,v in counter.items():
            if k=='l' or k=='o':
                counter[k]= v//2 # as we need 2 l and 2 o's
        balloon_counter = [v for k,v in counter.items() if k in list('balon')]
        ans = min(balloon_counter) if len(balloon_counter)==5 else 0
        return ans