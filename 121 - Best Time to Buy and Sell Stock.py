from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max = 0
#         days = len(prices)
#         for i in range(days):
#             for j in range(1+i, days):
#                 # print(f"{prices[i]} {prices[j]} = {prices[j]-prices[i]}")
#                 if prices[j]-prices[i] > max:
#                     max = prices[j] - prices[i]
#         return max


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        profit = 0
        for i in prices:
            if i < lowest_price:
                lowest_price = i
            if i - lowest_price > profit:
                profit = i - lowest_price
        return profit




prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [3,4,1,7,5]
# prices = [3,2,6,5,0,3]
print(Solution().maxProfit(prices))
