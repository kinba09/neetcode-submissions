class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        result = 0
        l = 0
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l+=1
            result = max(result, r-l+1)
            check.add(s[r])
        return result