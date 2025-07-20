class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row= len(matrix)
        col= len(matrix[0])
        z_row=set()
        z_col=set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    z_row.add(i)
                    z_col.add(j)

        for r in z_row:
            for a in range(col):
                matrix[r][a]=0
            
        for c in z_col:
            for b in range(row):
                matrix[b][c]=0
            
