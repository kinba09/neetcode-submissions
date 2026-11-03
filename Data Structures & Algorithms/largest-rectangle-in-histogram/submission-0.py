class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                oldi, oldh = stack.pop()
                maxarea = max(maxarea, oldh * (i-oldi))
                start = oldi
            stack.append((start,h))

        for i,h in stack:
            maxarea = max(maxarea, h*(len(heights)-i))
        return maxarea