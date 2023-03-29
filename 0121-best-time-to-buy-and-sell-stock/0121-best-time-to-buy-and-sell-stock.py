class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx = 0
        sell_idx = 1
        max_profit = 0
        num_prices = len(prices)
        while sell_idx < num_prices:
            # print(f'{buy_idx}:{sell_idx}')
            profit = prices[sell_idx] - prices[buy_idx]
            if profit > 0:
                max_profit = max(profit, max_profit)
            else:
                buy_idx = sell_idx #buy price should always be the minimum 
            sell_idx += 1

        return max_profit