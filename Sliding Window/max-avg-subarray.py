#lc easy
#sliding window
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        max_avg = -inf
        curr_sum = 0
        for end in range(len(nums)):
            curr_sum += nums[end]
            if end >= k-1:
                max_avg = max(max_avg,curr_sum/k)
                curr_sum -= nums[start]
                start += 1
        return max_avg
                