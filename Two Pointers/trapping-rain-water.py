#lc medium
#vviq
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0,len(height)-1
        maxL,maxR = height[l],height[r]
        res = 0
        while(l<r):
            if maxL <= maxR:
                l += 1
                maxL = max(maxL,height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR,height[r])
                res += maxR - height[r]
        return 0 if len(height) == 0 else res
