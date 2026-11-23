class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify_max(heap)
        window = {}
        for i in range(k):
            num = nums[i]
            window[num] = window.get(num,0)+1
            heapq.heappush_max(heap,num)
        res = []
        out = heap[0]
        res.append(out)
        for i in range(1,len(nums)-k+1):
            s_num = nums[i-1]
            e_num = nums[i+k-1]
            window[s_num]-=1
            window[e_num]=window.get(e_num,0)+1
            if window[s_num]==0:
                if s_num==out:
                    heapq.heappop_max(heap)
                del window[s_num]
            heapq.heappush_max(heap,e_num)
            # print(heap)
            while heap and heap[0] not in window:
                heapq.heappop_max(heap)
            out = heap[0]
            res.append(out)
        return res
