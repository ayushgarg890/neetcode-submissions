class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        minB = prices[0]

        for price in prices:
            ans=max(ans,price-minB)
            minB = min(minB,price)
        
        return ans