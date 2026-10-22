class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = defaultdict(int)
        for i,val in enumerate(nums):
            if (target - val) in check:
                return [check[target-val], i]
            check[val] = i
        