#lc hard
#Given two strings s and t of lengths m and n respectively,return the minimum window substring of s such that every character in t (including duplicates) 
#is included in the window. If there is no such substring, return the empty string "".

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tMap, sMap = {},{}
        l = 0
        res = inf
        rest = ''
        for i in range(len(t)):
            tMap[t[i]] = 1 + tMap.get(t[i],0)
        need, have = len(tMap), 0
        for r in range(len(s)):
            sMap[s[r]] = 1 + sMap.get(s[r],0)
            if s[r] in tMap and tMap[s[r]] == sMap[s[r]]:
                have += 1
            while(have == need):
                if r-l+1 < res:
                    res = r-l+1
                    rest = s[l:r+1]
                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        return rest
