class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        missing = len(t) 
        minlen = float('inf')
        l=0

        count = defaultdict(int)
        for i in t:
            count[i] +=1
        
        for r in range(len(s)):
            if count[s[r]] > 0:
                missing -=1
            count[s[r]] -=1

            while missing == 0:
                if (r-l+1) < minlen:
                    minlen = r-l+1
                    start = l

                count[s[l]] +=1
                if count[s[l]] > 0:
                    missing +=1
                l+=1
        return s[start:start+minlen] if minlen != float('inf') else ""

