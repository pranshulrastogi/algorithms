'''
Problem Link: https://leetcode.com/problems/4sum/
Difficulty: Medium
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        ans = set() # to avoid the similar groups
        for i in range(l-3):
            # to fix first number
            si = nums[i]
            if si >= 0 and si> target:
                break
            
            for j in range(i+1, l-2):
                # loop to fix 2nd number
                sj = si+nums[j]
                if sj >= 0 and sj > target:
                    
                    break
                
                for k in range(j+1, l-1):
                    # loop to fix 3rd number
                    sk = sj + nums[k]
                    if sk >= 0 and sk >  target:
                        # print(sk)
                        break
                    
                    li = k+1
                    while li < l:
                        news = sk+nums[li]
                        if news > target:
                            break
                        elif news == target:
                            ans.add((nums[i], nums[j], nums[k], nums[li]))
                        li+=1
        ans = [list(ele) for ele in ans]
        print(ans)
        return ans