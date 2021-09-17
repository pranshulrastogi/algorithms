'''
Problem link: https://leetcode.com/problems/slowest-key/
Difficulty: Easy
'''
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        time = [releaseTimes[0]] + [releaseTimes[i] - releaseTimes[i-1] for i in range(1,n)]
        time_key = list(zip(time,keysPressed))
        time_key.sort(key=lambda x:(x[0],x[1]))
        ans = time_key[-1][1]
        return ans