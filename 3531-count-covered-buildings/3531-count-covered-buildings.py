from collections import defaultdict
from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)

        pack = lambda x, y: x * (n + 1) + y

        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)

        status = {}   

        for x, ys in rows.items():
            if len(ys) < 3:
                continue
            ys.sort()
        
            base = x * (n + 1)
            for y in ys[1:-1]:
                k = base + y
                status[k] = status.get(k, 0) | 1

        for y, xs in cols.items():
            if len(xs) < 3:
                continue
            xs.sort()
            for x in xs[1:-1]:
                k = x * (n + 1) + y
                status[k] = status.get(k, 0) | 2

        cnt = 0
        for x, y in buildings:
            if status.get(pack(x, y), 0) == 3:
                cnt += 1
        return cnt
