#lc medium
#vviq
#O(n)
'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while (r > l):
            if numbers[r] + numbers[l] == target:
                return [l+1,r+1]
            elif numbers[r] + numbers[l] > target:
                r -=1
            else:
                l += 1

#Usual 2 sum, the array is not sorted, so we need to use a different approach using a hash map

import itertools
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        dict = {}
        for i, number in enumerate(nums):
            if (target-number in dict.keys()):
                return [dict[target-number],i]
            else:
                dict[number] = i