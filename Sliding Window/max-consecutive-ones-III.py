#lc medium
#sliding window
#Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        count = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            while(nums[r] == 0 and count>k):
                if nums[l] == 0:
                    count -= 1
                l += 1
            res = max(res,r-l+1)
        return res
         
