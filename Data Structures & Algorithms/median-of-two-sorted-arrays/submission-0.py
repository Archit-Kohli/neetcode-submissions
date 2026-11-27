class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m<=n:
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
            m,n = n,m

        start = 0
        end = len(A)
        while start<=end:
            x = (start+end)//2
            half = (m+n)//2
            rem = half-x
            # print(A,x)
            # print(B,rem)
            A_left = A[x - 1] if x>0 else float('-inf')
            A_right = A[x] if x<len(A) else float('inf')
            B_left = B[rem-1] if rem>0 else float('-inf')
            B_right = B[rem] if rem<len(B) else float('inf')
            if A_left<=B_right and B_left<=A_right:
                if (m+n)%2==0:
                    return (max(A_left,B_left)+min(A_right,B_right))/2
                else:
                    return min(A_right,B_right)
            elif A_left>B_right:
                end = x-1
            elif B_left>A_right:
                start = x+1
        return 



    