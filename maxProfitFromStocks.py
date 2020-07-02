class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value=float('inf')
        max_profit=0
        for i in range(len(prices)):
            if prices[i]<min_value:
                min_value=prices[i]
            elif prices[i]-min_value>max_profit:
                max_profit=prices[i]-min_value
        return max_profit