class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max_profit = 0

        if len(prices) <= 1:
            return 0
        
        min_price = prices[0]
        min_price_idx = 0
        max_price = 0
        max_diff = 0
        for i in range(1, len(prices)):
            # optimal buy
            if prices[i] < min_price:
                min_price = prices[i]
                min_price_idx = i
                max_price = 0
            
            # optimal sale
            if prices[i] > max_price and i > min_price_idx:
                max_price = prices[i]
                max_diff = max(max_diff, max_price - min_price)
        
        return max_diff