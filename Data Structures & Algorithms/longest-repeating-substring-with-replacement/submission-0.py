class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = defaultdict(int)
        maxf = 0
        l = 0
        res = 0

        for r in range(len(s)):
            check[s[r]] +=1
            maxf = max(maxf, check[s[r]])

            while (r-l+1) - maxf > k:
                check[s[l]] -=1
                l +=1
            res = max(res, (r-l+1))
        return res