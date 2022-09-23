#lc easy
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        op = []
        while (r >= l):
            if pow(nums[l],2) > pow(nums[r],2):
                op.append(pow(nums[l],2))
                l += 1
            else:
                op.append(pow(nums[r],2))
                r -= 1
        return op[::-1]

#Using python in built methods

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=[x**2 for x in nums]
        nums.sort()
        return nums
                
            
        