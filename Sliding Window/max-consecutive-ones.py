#lc easy
#sliding window
#Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        res = 0
        for r in range(len(nums)):
            while(nums[r] == 0):
                l = r+1
                nums[r] = '_'
            res = max(res, r-l+1)
        return res
        
