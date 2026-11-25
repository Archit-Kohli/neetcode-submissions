class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBan = max(piles)
        start = 1
        end = maxBan
        out = end
        while start<=end:
            mid = (start+end)//2
            count = 0
            for p in piles:
                count+=math.ceil(p/mid)
            if count<=h:
                out = mid
                end = mid-1
            else:
                start=mid+1
        return out