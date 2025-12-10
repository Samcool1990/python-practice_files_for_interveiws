#Leetcode 121
# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


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
prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))



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

print(maxProfit2(prices))