class Solution:
   def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)

        COLS = len(grid[0])

        visited = set()

        islands = 0

        directions = [

            [0, 1],

            [0, -1],

            [1, 0],

            [-1, 0]

        ]

        def bfs(r, c):

            q = deque()

            q.append((r, c))

            visited.add((r, c))

            while q:

                row, col = q.popleft()

                for dr, dc in directions:

                    nr = row + dr

                    nc = col + dc

                    if (nr < 0 or nc < 0 or

                        nr >= ROWS or nc >= COLS or

                        grid[nr][nc] == "0" or

                        (nr, nc) in visited):

                        continue

                    q.append((nr, nc))

                    visited.add((nr, nc))

        for r in range(ROWS):

            for c in range(COLS):

                if grid[r][c] == "1" and (r, c) not in visited:

                    islands += 1

                    bfs(r, c)

        return islands