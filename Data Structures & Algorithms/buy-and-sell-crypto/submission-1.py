class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two Pointer Approach
       i = 0
       n = len(prices)
       j = i+1
       max_profit = 0
       while(i<j<n):
            buy = prices[i]
            sell = prices[j]
            if buy<sell:
                curr_profit = sell-buy
                max_profit =  max(max_profit, curr_profit)
                j+=1
            elif buy >= sell:
                i=j
                j+=1
       return max_profit
    

            


