class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in range(len(nums)):
            counts[nums[i]]+=1
        heap = []
        for key in counts:
            heapq.heappush_max(heap,[counts[key],key])
        out = []
        for j in range(k):
            out.append(heapq.heappop_max(heap)[1])
        return out