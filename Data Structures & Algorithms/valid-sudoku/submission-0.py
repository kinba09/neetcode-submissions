class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sq = defaultdict(set)

        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == '.':
                    continue
                if x in row[i] or x in col[j] or x in sq[(i//3, j//3)]:
                    return False
                
                row[i].add(x)
                col[j].add(x)
                sq[(i//3,j//3)].add(x)
        return True