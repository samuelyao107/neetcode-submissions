class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max=0
        j=0
        for i in range(1,n):
            if prices[j] < prices[i]:
                if prices[i]-prices[j]>max:
                    max= prices[i]-prices[j]
            else:
                j=i        
            

        return max          