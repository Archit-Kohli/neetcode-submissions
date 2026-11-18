class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProduct = [1]*(n+1)
        suffixProduct = [1]*(n+1)
        for i in range(n):
            prefixProduct[i+1] = prefixProduct[i]*nums[i]
        for i in range(n,0,-1):
            suffixProduct[i-1] = suffixProduct[i]*nums[i-1]
        # print(prefixProduct)
        # print(suffixProduct)
        out = []
        for i in range(n):
            out.append(prefixProduct[i]*suffixProduct[i+1])
        return out