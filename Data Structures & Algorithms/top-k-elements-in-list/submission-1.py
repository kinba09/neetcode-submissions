class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = Counter(nums)
        group = [[] for _ in range(len(nums)+1)]

        for val,num in count.items():
            group[num].append(val)

        for i in range(len(group)-1, -1, -1):
            for j in group[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans
        return ans