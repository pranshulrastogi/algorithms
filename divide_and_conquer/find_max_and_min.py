'''
finds maximum and minimum in an array using divide and conquer
Input: An array of n integers
Output: (maximum, minimum)
'''

from typing import List
import random


def max_and_min(arr: List[int], p: int, q: int) -> List[int]:
    # p denotes starting index
    # q denotes ending index
    # 
    if q-p == 0: # only one element
        return [arr[p], arr[p]]
    elif q-p == 1: # only 2 element
        return [max(arr[p],arr[q]), min(arr[p],arr[q])]

    elif p > q: # not possible
        return None

    else:
        # more than 2 elements exist, 
        # divide the problem

        # DIVIDE STEP
        mid = (p+q)//2

        # CONQUER STEP
        local_max_left, local_min_left = max_and_min(arr, p, mid)
        local_max_right, local_min_right = max_and_min(arr, mid+1, q)

        # MERGE STEP
        local_max = max(local_max_left, local_max_right)
        local_min = min(local_min_left, local_min_right)
        return [local_max, local_min]



if __name__ == "__main__":
    arr = [random.randrange(1,20) for i in range(5)]
    print(f"finding max and min in arr:\n{arr}")
    mx, mn = max_and_min(arr, 0, len(arr)-1)
    print(f"max:{mx}\nmin:{mn}")
        
