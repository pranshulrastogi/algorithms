'''
This algorithm is partial implementation of divide and conquer

I/p: array of unsorted integers and k
O/P: return kth smallest element in given array
T.C: W.C: O(n*n) but A.C: O(n)
'''

from quick_sort import partition
from random import randint


def selection_procedure(arr, k, *args, **kwargs):
    if 'p' in kwargs:
        p=kwargs['p']
    else:
        p=0
    if 'q' in kwargs:
        q=kwargs['q']
    else:
        q=len(arr)-1
    if p==q:
        if p==k:
            return arr[p]
        else:
            return -1
    elif p>q:
        return -1
    
    else:
        # we will use quick sort's partition algorithm
        # as we know that it returns rth smallest element
        r,_ = partition(arr, p, q)  # will return the rth smallest element
        if r==k: # this is the kth smallest element
            return arr[r]
        elif r < k:
            # go right
            return selection_procedure(arr, k, p=r+1, q=q)
        else:
            # go left
            return selection_procedure(arr, k, p=p, q=r-1)


if __name__ == "__main__":
    arr = [randint(1,500) for i in range(20)]
    print(f"finding 1st smallest element in {arr}")
    ele = selection_procedure(arr, 0)
    ele2 = min(arr) # for verifying 
    print(ele, ele2)


    
