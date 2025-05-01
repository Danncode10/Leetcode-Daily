class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit





# prices = [7,1,5,3,6,4]
#
# n = len(prices)
# min_index_value = prices[0]
# min_index = 0
# max_index = 0
# count_decrease = 0  # This is used if the array is from highest to lowest, then you cant have profit, you cant buy if count_decrease == n
#
# # Note: the max_index cannot be lesser than min_index_value
#
# for i in range(n):
#     if prices[i] < min_index_value:
#         count_decrease += 1
#         min_index = i
#         min_index_value = prices[i]
#
# # To find the max index, starts at lowest index
# max_index = min_index
# max_index_value = prices[min_index]
# for i in range(min_index, n):
#     if prices[i] > max_index_value:
#         max_index_value = prices[i]
#         max_index = i
#
# print("Result: ", end='')
#
# if count_decrease == n:
#     print(0)
# else:
#     print(max_index_value - min_index_value)