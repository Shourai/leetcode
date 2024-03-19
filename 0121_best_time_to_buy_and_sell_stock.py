class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0

        for i in prices:
            if i < lowest_price:
                lowest_price = i
            elif i - lowest_price > max_profit:
                max_profit = i - lowest_price

        return max_profit


def case_one():
    prices = [7, 1, 5, 3, 6, 4]
    output = 5
    assert (Solution().maxProfit(prices)) == output


def case_two():
    prices = [7, 6, 4, 3, 1]
    output = 0
    assert (Solution().maxProfit(prices)) == output


def case_three():
    prices = [1, 2]
    output = 1
    assert (Solution().maxProfit(prices)) == output


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
