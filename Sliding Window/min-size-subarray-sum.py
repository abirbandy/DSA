#Sliding window
#lc medium
#Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = inf
        start=0
        sum=0
        for end in range(len(nums)):
            sum += nums[end]
            if sum >= target:
                while (sum >= target):
                    #here we do +1 because we need to find length
                    min_length = min(min_length,end-start+1)
                    sum -= nums[start]
                    start +=1
            end += 1
        return 0 if min_length == inf else min_length