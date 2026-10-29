
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    continue

                stack = [(r, c)]
                grid[r][c] = 0
                area = 0

                while stack:
                    x, y = stack.pop()
                    area += 1

                    for dx, dy in [
                        (1, 0), (-1, 0),
                        (0, 1), (0, -1)
                    ]:
                        nx, ny = x + dx, y + dy

                        if (0 <= nx < rows and
                            0 <= ny < cols and
                            grid[nx][ny] == 1):

                            grid[nx][ny] = 0
                            stack.append((nx, ny))

                max_area = max(max_area, area)

        return max_area
