class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        start = 0
        end = m*n-1
        while start<=end:
            mid = (start+end)//2
            midPo = [mid//n,mid%n]
            midP = matrix[midPo[0]][midPo[1]]
            if midP==target:
                return True
            if midP<target:
                start=mid+1
            else:
                end=mid-1
        return False

        # 5 4