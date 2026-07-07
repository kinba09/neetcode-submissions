class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        check = defaultdict(int)

        for i,val in enumerate(nums):
            diff = target - val
            if diff in check:
                return [check[diff],i]
            check[val] = i
        




