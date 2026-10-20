class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_set = set(nums)

        for r in nums_set:
            if (r - 1) not in nums_set:
                length = 1
                while r + 1 in nums_set:
                    length +=1
                    r +=1
                result = max(result, length)
        return result