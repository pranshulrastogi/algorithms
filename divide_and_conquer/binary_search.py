'''
input: A sorted array of n elements, and 'x' -item to be searched
Output: position of x, if x is present, else return -1
'''

from typing import List


def bs(arr: List, starting_index: int, ending_index: int, x: int) -> int:
    p = starting_index
    q = ending_index
    
    # check if only one element in array
    if p==q:
        # check if this is the 'x', else return -1
        if arr[p] == x:
            return p
        else:
            return -1
    else:
        # divide step
        mid = (p+q)//2

        # check if mid is the element
        if arr[mid] == x:
            return mid
        elif x > arr[mid]: # element, if present, must be on right side of mid
            return bs(arr, mid+1, q, x)
        elif x < arr[mid]: # element, if present, must be on lesser(left) side of mid
            return bs(arr, p, mid-1, x)

if __name__ == "__main__":
    arr = [x for x in range(2,50,2)]

    print(f"Searching 5 in {arr}")
    print(bs(arr, 0, len(arr), 5))
    print(f"Searching 10 in {arr}")
    print(bs(arr, 0, len(arr), 10))
