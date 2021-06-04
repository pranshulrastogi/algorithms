'''
752. Open the Lock
Link: https://leetcode.com/problems/open-the-lock/
Difficulty: Medium

Problem Statement:
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
The wheels can rotate freely and wrap around: for example 
we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, 
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the 
minimum total number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".

'''

# well this is application of BFS,
# every node (ex: 0000) have 8 neighbors, 4 by going forward
# and 4 by moving backward for every i

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def neighbour(val):
            # this will generate neighbours for val
            for i in range(4):
                x = int(val[i])
                for diff in (-1,1):
                    y = (x+diff+10)%10
                    yield val[:i] + str(y) + val[i+1:]
        
        
        q = deque(['0000']) # get your queue populated
        deadset = set(deadends)
        if "0000" in deadset:
            return -1
        steps = 0
        while q:
            for _ in range(len(q)): # this is required to control steps, as all the child are at step 1
                val = q.popleft()
                if val == target:
                    return steps
                for n in neighbour(val):
                    if n in deadset: continue
                    deadset.add(n) # mark this node as visited
                    q.append(n)
            steps += 1
        return -1