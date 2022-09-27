#lc easy
'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''
#O(logn) time complexity also O(1) memory
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            res = 0
            while n:
                digit = n%10
                res += digit ** 2
                n = n//10
            return res
        
        slow = n
        fast = get_next(n)
        while fast != slow and fast != 1:
            fast = get_next(get_next(fast))
            slow = get_next(slow)
        return fast == 1

#O(logn) time complexity also O(n) memory
class Solution:
    def isHappy(self, n: int) -> bool:
        def squareofdigits(n):
            res = 0
            while n:
                digit = n%10
                res += digit ** 2
                n = n//10
            return res
        
        hashset = set()
        while n not in hashset:
            hashset.add(n)
            n = squareofdigits(n)
            if n == 1:
                return True
        return False
      

