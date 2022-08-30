# 08/30/2022 10:56	Accepted	40 ms	14 MB	python3
# cheated a bit and looked up the transformations
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        # flip along main diagonal
        for i in range(0, m):
            for j in range(i, n):
                if i == j:
                    continue
                val = matrix[i][j]
                val2 = matrix[j][i]     
                matrix[i][j] = val2
                matrix[j][i] = val
        
        # flip l->r
        for j in range(0, int(n / 2)):
            for i in range(0, m):
                j2 = n - 1 - j
                val = matrix[i][j]
                val2 = matrix[i][j2]
                matrix[i][j] = val2
                matrix[i][j2] = val
