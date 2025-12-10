from typing import List

MOD = 10**9 + 7

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        res = 1
        for x in range(1, n):
            res = res * x % MOD

        return res
