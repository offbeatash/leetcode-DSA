class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r,c, visited):
            visited.add((r,c))

            directions = [
                (0,1), (0,-1),
                (1,0), (-1,0)
            ]

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if not(0 <= nr < rows and 0 <= nc < cols):
                    continue

                if (nr, nc) in visited:
                    continue


                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc, visited)

        for c in range(cols):
            dfs(0,c,pacific)

        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(rows-1, c, atlantic)

        for r in range(rows):
            dfs(r, cols-1, atlantic)

        result = []

        for r,c in pacific:
            if (r,c) in atlantic:
                result.append([r,c])
            
        return result
