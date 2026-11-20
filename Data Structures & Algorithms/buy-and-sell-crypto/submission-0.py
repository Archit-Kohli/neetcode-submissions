class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSeen = float('inf')
        out = 0
        for i in range(len(prices)):
            minSeen = min(minSeen,prices[i])
            out = max(out, prices[i]-minSeen)
        return out