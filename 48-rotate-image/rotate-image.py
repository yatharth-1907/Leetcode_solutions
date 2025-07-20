class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col= len(matrix[0])
        temp_mat=[[0 for _ in range(col)] for _ in range(row)]
        
        for i in range(row-1,-1,-1):
            for j in range(col):
                temp_mat[j][col-1-i]= matrix[i][j]

        for i in range(row):
            for j in range(col):
                matrix[i][j]= temp_mat[i][j]
