class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [0,3,2,5,4,6,1,1]     
        if nums == []:
            return 0   
        heap = []
        for i in nums:
            heapq.heappush(heap,i)
        out = 1
        ele = {}
        while heap:
            i = heapq.heappop(heap)
            if i in ele:
                continue
            if i-1 in ele:
                out = max(out, ele[i-1]+1)
                ele[i]=ele[i-1]+1
            else:
                ele[i]=1
        return out
