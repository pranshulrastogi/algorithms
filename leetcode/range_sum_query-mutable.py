'''
Problem Link: https://leetcode.com/problems/range-sum-query-mutable/
Difficulty: Medium

Problem stmt:
Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

'''

# here I have used square root decomposition
# I divided the array into blocks of size sqrt(n)
# where n is the size of the array
# this way whenver update happens you have to perform
# maximum of sqrt(n) sum and updation
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.block_size = int(math.floor(math.sqrt(self.n)))
        print(f"block_size: {self.block_size}")
        self.block_count = math.ceil(self.n/self.block_size)
        self.block_sum = []
        j=0
        for i in range(self.block_count):
            print(f"block: {i}")
            if j+self.block_size < self.n:
                s = sum(self.nums[j:j+self.block_size])
                j += self.block_size
            else:
                s = sum(self.nums[j:])
                
            self.block_sum.append(s)
        print(*self.block_sum)
            
    def getblocknum(self, ind):
        block_num = ind//self.block_size
        return block_num
        

    def update(self, index: int, val: int) -> None:
        dif = val - self.nums[index]
        # get block
        block = self.getblocknum(index)
        self.block_sum[block] += dif
        self.nums[index] = val
        
        
        

    def sumRange(self, left: int, right: int) -> int:
        left_block = self.getblocknum(left)
        right_block = self.getblocknum(right)
        # get sum of all the blocks in the middle
        s=0
        for i in range(left_block, right_block+1):
            # print(f"adding block {i}")
            
            s+= self.block_sum[i]
        # process left_block
        left_si = left_block * self.block_size
        right_ei = ((right_block+1) * self.block_size) -1 
        if right_ei >= self.n:
            right_ei = self.n-1
        for i in range(left_si, left):
            s-= self.nums[i]
        for i in range(right+1, right_ei+1):
            s -= self.nums[i]
        return s

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)