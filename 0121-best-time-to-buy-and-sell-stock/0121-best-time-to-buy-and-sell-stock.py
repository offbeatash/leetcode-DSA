class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0

        for price in prices[1:]:
            if price < low:
                low = price
            elif price - low > profit:
                profit = price - low

        return profit