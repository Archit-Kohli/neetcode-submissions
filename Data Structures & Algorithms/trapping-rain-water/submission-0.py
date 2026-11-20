class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefixMax = [0]*(n+1)
        suffixMax = [0]*(n+1)
        for i in range(1,n+1):
            prefixMax[i] = max(prefixMax[i-1],height[i-1])
        for i in range(n,-1,-1):
            suffixMax[i-1] = max(suffixMax[i],height[i-1])
        out = 0
        # 0 0 2 2 3 3 3 3 3 3 3
        # 3 3 3 3 3 3 3 3 2 1 0
        for i in range(n):
            out+=min(prefixMax[i+1],suffixMax[i])-height[i]
        return out
            
