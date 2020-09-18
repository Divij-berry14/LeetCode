import sys
def maxProfit(prices):
    mini = sys.maxsize
    profit = 0
    for i in range(len(prices)):
        if mini > prices[i]:
            mini = prices[i]
        elif profit < prices[i] - mini:
            profit = prices[i] - mini
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))