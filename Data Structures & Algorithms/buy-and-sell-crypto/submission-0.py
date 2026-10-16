class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        mini = prices[0]

        for sell in prices:
            maxp = max(maxp, sell - mini)
            mini = min(sell, mini)
        return maxp