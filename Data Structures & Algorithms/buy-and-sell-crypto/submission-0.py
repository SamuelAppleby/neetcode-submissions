class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax = 0
        buy = prices[0]
        sell = -1

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]

            elif prices[i] - buy > currentMax:
                currentMax = prices[i] - buy

        return currentMax