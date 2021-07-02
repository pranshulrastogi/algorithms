'''
Problem link: https://leetcode.com/problems/find-k-closest-elements/
Difficulty: Medium
Problem stmt:
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from sortedcontainers import SortedList
        import bisect
        n = len(arr)
        lst = SortedList()
        idx = bisect.bisect_left(arr, x) # get the left bound
        if idx < n and arr[idx] == x:
            lst.add(x)
            left = idx-1
            right = idx+1
            k-=1
        elif idx == n:
            left = idx-1
            right = idx
        else:
            left = idx-1
            right = idx
        
        
        while k > 0:
            if left >= 0 and right < n:
                dif_l = x-arr[left]
                dif_r = arr[right] - x
                if dif_l <= dif_r:
                    ele = arr[left]
                    left -= 1
                else:
                    ele = arr[right]
                    right += 1
            elif left >= 0:
                ele = arr[left]
                left -=1
            else:
                ele = arr[right]
                right += 1
            lst.add(ele)
            k -=1
        return lst