class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            hashset = set()
            for i in row:
                if i == ".":
                    continue
                if i in hashset:
                    return False
                hashset.add(i)
        
        for i in range(len(board)):
            hashset = set()
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue
                if board[j][i] in hashset:
                    return False
                hashset.add(board[j][i])
        
        for square in range(9):
            hashset = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in hashset:
                        return False
                    hashset.add(board[row][col])
        
        return True


                

