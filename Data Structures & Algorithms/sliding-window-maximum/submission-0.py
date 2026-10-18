class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []
        l = 0
        for r in range(len(nums)):
            # remove out of bound
            if q and q[0] <= r-k:
                q.popleft()

            #update large number
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            if r-l+1 >= k:
                result.append(nums[q[0]])
                l+=1
        return result