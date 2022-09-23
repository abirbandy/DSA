#lc easy
'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
'''
#O(n)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if (nums[r] != nums[r-1]):
                nums[l] = nums[r]
                l += 1
        return l
        