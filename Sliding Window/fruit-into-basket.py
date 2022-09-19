#lc medium
#Sliding Window
#Longest Substring with K Distinct Characters where K=2.
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k = 2
        l = 0
        res = 0
        hashmap = {}
        for r in range(len(fruits)):
            if fruits[r] in hashmap:
                hashmap[fruits[r]] += 1
            else:
                hashmap[fruits[r]] = 1
            while(len(hashmap)>k):
                if hashmap[fruits[l]] == 1:
                    del hashmap[fruits[l]]
                else:
                    hashmap[fruits[l]] -= 1
                l += 1
            res = max(res,sum(hashmap.values()))
        return res