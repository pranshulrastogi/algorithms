'''
Input: a,b
Output: a^b or a**b 
T.C: log(b)*log(b)
'''

def get_nearest_power(p):
    '''
    Given p, returns nearest power of 2
    '''
    i=1
    while True:
        prod = 2**i
        if prod > p:
            # this is it, we reached power of 2 > p
            result = 2**(i-1), False
            break
        elif prod == p:
            result = prod, True
            break
        i+=1
    return result

def cal_power(a,b):
    '''
    Given a and b, calculates a^b using divide and conquer technique
    T.C: log(b)
    Assumption is 'b' will be power of 2, so we will enforce it in main function
    '''
    if b==1:
        return a
    
    mid = b//2 # divide step
    multiplication = cal_power(a,mid) # conquer step
    return multiplication * multiplication  # result step


if __name__ == "__main__":

    # get input
    a = input("Enter value of a: ")
    b = input("Enter value of b: ")
    a, b = int(a), int(b)

    # check if power of 2, if not get nearest and start calculating
    p = b
    ans = 1
    while p > 1:
        pow, isPower2 = get_nearest_power(p)
        ans *= cal_power(a,p)
        p -= pow
    ans = ans * a if p == 1 else ans
    print(ans)






    