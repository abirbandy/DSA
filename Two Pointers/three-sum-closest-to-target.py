#lc medium
'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        i = 0
        diff = inf
        res = 0
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == target:
                    return summ
                if abs(target-summ) < diff:
                    diff = abs(target-summ)
                    res = summ
                if summ > target:
                    r -= 1
                elif summ < target:
                    l += 1
        return res
                    
                
        