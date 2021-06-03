
from typing import List
import random


def merge(a1: List[int], a2: List[int]) -> List[int]:
    '''
    it merges 2 sorted subarrays and returns combined
    sorted array

    '''
    aux = [] # auxillary array
    i1 = 0
    i2 = 0

    l1 = len(a1)
    l2 = len(a2)

    while i1<l1 and i2<l2:
        if a1[i1] < a2[i2]:
            aux.append(a1[i1])
            i1 += 1
        else:
            aux.append(a2[i2])
            i2 += 1
    while i1<l1:
        aux.append(a1[i1])
        i1 += 1
    
    while i2 < l2:
        aux.append(a2[i2])
        i2 += 1
    
    return aux

def merge_sort(arr: List[int], p: int, q: int) -> List[int]:
    '''
    sorts the arr, with starting index as p and ending index as q

    '''
    # it uses divide and conquer technique
    # first lets cover the termination conditions
    
    # if there is only one element, it is already sorted, so return it
    if p==q:
        return [arr[p]]
    
    # if starting index is greater than ending index, its a negative check
    if p > q:
        return arr
    
    # lets start merge sort algorithm

    # STEP1 divide
    mid = (p+q)//2

    # STEP2 conquer
    arr_left = merge_sort(arr, p, mid)
    arr_right = merge_sort(arr, mid+1, q)

    # STEP3 merge
    # merging 2 sorted subarrays arr_left and arr_right
    sorted_arr = merge(arr_left, arr_right)
    
    return sorted_arr

def sort(arr: List[int]) -> List[int]:
    '''
    Given unsorted array 'arr', it returns sorted 'arr'
    '''

    # call merge_sort to sort the array
    return merge_sort(arr, 0, len(arr)-1)


# main 
if __name__ == "__main__":
    arr = [random.randint(10,1000) for i in range(20)]
    print(f"sorting arr:\n{arr}")
    s = sort(arr)
    print(f"sorted arr:\n{s}")