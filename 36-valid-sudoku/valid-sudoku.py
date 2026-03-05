class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # valid=True
        row= [[],[],[],[],[],[],[],[],[]]
        col= [[],[],[],[],[],[],[],[],[]]
        inner=[[],[],[],[],[],[],[],[],[]]
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]=='.':
                    pass
                else:
                    if not row[j]:
                        row[j].append(board[i][j])
                    elif (board[i][j] in  row[j]):
                        return False
                    else:
                        row[j].append(board[i][j])

                    if not col[i]:
                        col[i].append(board[i][j])
                    elif (board[i][j] in  col[i]):
                        return False
                    else:
                        col[i].append(board[i][j])
                    
                    if not inner[(i//3)*3+(j//3)]:
                        inner[(i//3)*3+(j//3)].append(board[i][j])
                    elif board[i][j] in inner[(i//3)*3+(j//3)]:
                        return False
                    else:
                        inner[(i//3)*3+(j//3)].append(board[i][j])
        return True