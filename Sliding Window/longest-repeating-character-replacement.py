#lc medium
#sliding window
#You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        l = 0
        count = 0
        for r in range(len(s)):
            if s[r] not in dic:
                dic[s[r]] = 1
            else:
                dic[s[r]] += 1
            # we are checking if the difference between the the substring length and the frequency of char occuring the most is more than permissible replacement limit
            while((r-l+1)- max(dic.values())) > k:
                if dic[s[l]] == 1:
                    del dic[s[l]]
                else:
                    dic[s[l]] -= 1
                l += 1
            count = max(count,r-l+1)
        return count
