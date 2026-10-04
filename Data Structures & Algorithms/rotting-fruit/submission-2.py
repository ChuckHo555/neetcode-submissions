class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r, c))
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        while q and fresh>0:
            length = len(q)
            for i in range(length):
                currentRow, currentColumn = q.popleft()
                for rowDirection, columnDirection in directions:
                    newRow, newColumn = currentRow + rowDirection, currentColumn + columnDirection 
                    if(newRow in range(len(grid)) and newColumn in range(len(grid[0])) and grid[newRow][newColumn] == 1):
                        grid[newRow][newColumn] =2
                        q.append((newRow, newColumn))
                        fresh-=1
            time +=1
        return time if fresh == 0 else -1