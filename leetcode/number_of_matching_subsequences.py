'''
Link: https://leetcode.com/problems/number-of-matching-subsequences/
difficulty: Medium
Problem:
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
'''

from collections import defaultdict
import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        '''
        for every string in words, check with s
        '''
        l = len(s)
        count=0
        mapping = defaultdict(list)
        # define mapping
        for i,c in enumerate(s):
            mapping[c].append(i)
        
        for word in words:
            flag=True
            prev = -1
            for c in word:
                # find the index of the character c in mapping and get the best fit using bisect(binary search and get the right index)
                ind = bisect.bisect(mapping[c],prev)
                if ind >= len(mapping[c]):
                    flag=False
                    break
                prev = mapping[c][ind]
            if flag:
                count+=1
        print(count)
        return count