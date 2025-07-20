class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row= len(matrix)
        col= len(matrix[0])
        top, bottom, left, right= 0, row-1, 0, col-1
        ans=[]

        while left<=right and top<=bottom:

            for lr in range(left,right+1):
                ans.append(matrix[top][lr])
            top+=1

            for tb in range(top,bottom+1):
                ans.append(matrix[tb][right])
            right-=1

            if top<=bottom:
                for rl in range(right,left-1,-1 ):
                    ans.append(matrix[bottom][rl])
                bottom-=1

            if left<=right:
                for bt in range(bottom,top-1,-1):
                    ans.append(matrix[bt][left])
                left+=1

        return ans

