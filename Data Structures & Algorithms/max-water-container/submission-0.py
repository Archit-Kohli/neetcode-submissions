class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out = 0
        start = 0
        end = len(heights)-1
        while start < end:
            minH = min(heights[start],heights[end])
            width = end-start
            area = minH*width
            out = max(out,area)
            if heights[start]<=heights[end]:
                start+=1
            else:
                end-=1
        return out
