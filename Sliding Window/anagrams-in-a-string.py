#lc medium
#Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pMap = {}
        sMap = {}
        l = 0
        op = []
        for i in range(len(p)):
            pMap[p[i]] = pMap.get(p[i],0) + 1
        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r],0) + 1
            while(sum(sMap.values()) == len(p)):
                if(sMap == pMap):
                    op.append(l)
                if sMap[s[l]] == 1:
                    sMap.pop(s[l])
                else:
                    sMap[s[l]] -= 1
                l += 1
        return op
        
