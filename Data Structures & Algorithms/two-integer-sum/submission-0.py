class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            newtarget = target - nums[i]
            if newtarget in seen:
                return [seen[newtarget],i]
            seen[nums[i]]=i    
