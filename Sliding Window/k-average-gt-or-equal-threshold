#lc medium
#sliding window
#Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        summ = 0
        count = 0
        for i in range(len(arr)):
            summ += arr[i]
            if i >= k-1:
                if summ/k >= threshold:
                    count+=1
                summ -= arr[start]
                start += 1
        return count
                    
