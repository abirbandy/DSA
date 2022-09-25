#lc easy
#actually very difficult
#vvip
'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i,j = len(s)-1,len(t)-1
        countS, countT = 0,0
        while (i>=0 or j>=0):
            while(i >= 0):
                if s[i] == "#":
                    countS += 1
                elif countS > 0:
                    countS -= 1
                else:
                    break
                i -= 1
            while(j >= 0):
                if t[j] == "#":
                    countT += 1
                elif countT > 0:
                    countT -= 1
                else:
                    break
                j -= 1 
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True
