class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [] 
        for i in range(len(nums)+1):
            ans.append([]) 
        nums_count = Counter(nums)

        for i,val in nums_count.items():
            ans[val].append(i)
        
        result = []
        for i in range(len(ans)-1,0,-1):
            for j in ans[i]:
                result.append(j)
                if len(result) == k:
                    return result
        