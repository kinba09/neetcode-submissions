class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opp = {'(':')',
                '{':'}',
                '[':']'}
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    return False
                if opp[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return not stack