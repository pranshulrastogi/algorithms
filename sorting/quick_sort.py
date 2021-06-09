'''
Quick sort, T.C.: bestcase O(nlogn), worst case O(n**2)
Input: array of integers, arr
output: sorted array

-> one of the best algorithm
-> life of this algorithm lies in its 'partition' procedure i.e. "divide" step 
-> Stable algorithm
-> inplace
'''

import random
from typing import List


def partition(a: List[int], p: int, q: int):
    '''
    Given array a, with starting index as p and ending index as q
    it places a[p] in its rightful place in sorted manner and returns
    its index, and array itself
    '''
    if p==q:
        return [p, a]
    elif p > q:
        return [p, a]

    else:
        x = a[p] # pivot element
        i=p
        for j in range(i+1, q+1):
            if a[j] < x: # keep smaller elements on left of pivot
                i+=1
                a[i], a[j] = a[j], a[i] #swap
        # at last swap ith element with pivot
        a[p], a[i] = a[i], a[p]
        return [i, a]

def quick_sort(arr, p, q):
    if p>=q:
        return arr
    else:
        #divide step
        r, arr = partition(arr, p, q)
        # conquer step
        arr = quick_sort(arr, p, r-1)
        arr = quick_sort(arr, r+1, q)
        return arr





def sort(arr):
    # run quick sort
    return quick_sort(arr, 0, len(arr)-1)

if __name__ == "__main__":
    arr = [random.randint(5,500) for i in range(10)]
    print(f"sorting {arr}")
    sort_arr = sort(arr)
    print(f"sorted: {sort_arr}")

