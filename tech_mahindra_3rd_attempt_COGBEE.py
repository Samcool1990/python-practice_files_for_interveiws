#Leetcode 121

import math
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sellOne = 0
        holdOne = -math.inf

        for price in prices:
            sellOne = max(sellOne, holdOne + price)
            holdOne = max(holdOne, -price)
        
        return sellOne
    




def maxProfit2(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update the minimum price seen so far
        min_price = min(min_price, price)
        # Calculate the profit if we sell at the current price
        profit = price - min_price
        # Update the maximum profit
        max_profit = max(max_profit, profit)

    return max_profit

