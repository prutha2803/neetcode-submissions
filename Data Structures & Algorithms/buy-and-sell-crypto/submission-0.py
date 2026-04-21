class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price= prices[0]
        max_profit=0

        for i in range(1, len(prices)):
            p=prices[i]

            if p< min_price:
                min_price= p
            else:
                profit= p - min_price
                max_profit= max(profit, max_profit)

        return max_profit

        