#lc medium
#Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        pMap = {}
        sMap = {}
        l = 0
        for i in range(len(s1)):
            pMap[s1[i]] = 1 + pMap.get(s1[i],0)
        for r in range(len(s2)):
            sMap[s2[r]] = 1 + sMap.get(s2[r],0)
            while(sum(sMap.values()) == len(s1)):
                if pMap == sMap:
                    return True
                if sMap[s2[l]] == 1:
                    sMap.pop(s2[l])
                else:
                    sMap[s2[l]] -= 1
                l += 1 
        return False
