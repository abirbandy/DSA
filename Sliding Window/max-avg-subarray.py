#lc easy
#sliding window
#You are given an integer array nums consisting of n elements, and an integer k.
#Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        res = -inf
        summ = 0
        for r in range(len(nums)):
            summ += nums[r]
            if r-l+1 == k:
                res = max(res,summ/k)
                summ -= nums[l]
                l += 1
        return res
                