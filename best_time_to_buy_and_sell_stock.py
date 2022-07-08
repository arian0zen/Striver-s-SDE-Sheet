'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
#well there is an obvious solution that is a brute force solution.
#rather we will use, sliding window technique
# here window low is low pointer and i in window high pointer

def maxProfit(prices):
    max_count = 0
    window_low = 0
    for i in range (len(prices)):
        max_count = max(max_count, prices[i] - prices[window_low]) 
        if prices[i] < prices[window_low]: #if prices[i] > prices[window_low] that means there are lesser price available to buy the stock
            window_low = i #changing that to start and then start count from that buying price        
    return max_count
    
prices = [7,1,5,3,6,4]
print(maxProfit(prices))