class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        if nums[end]>=nums[start]:
            return nums[0]
        out = float('inf')
        while start<=end:
            mid = (start+end)//2
            # print(nums[start],nums[end],nums[mid])
            if nums[mid]>=nums[start]:
                out = min(nums[start],out)
                start = mid+1
            else:
                out = min(nums[end],out)
                end = mid
        return out