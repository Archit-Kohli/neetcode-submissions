class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def twoSum(l, t, i):
            s = i + 1
            e = len(l) - 1
            pairs = []
            while s < e:
                if l[s] + l[e] == t:
                    pairs.append([s, e])
                    s += 1
                    e -= 1
                    # Skip duplicate values for s and e
                    while s < e and l[s] == l[s - 1]:
                        s += 1
                    while s < e and l[e] == l[e + 1]:
                        e -= 1
                elif l[s] + l[e] < t:
                    s += 1
                else:
                    e -= 1
            return pairs

        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            out = twoSum(nums, -nums[i], i)
            for pair in out:
                res.append([nums[pair[0]], nums[pair[1]], nums[i]])
                
        return res