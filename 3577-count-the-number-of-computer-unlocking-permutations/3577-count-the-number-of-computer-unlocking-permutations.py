MOD = 10**9 + 7

class Solution:
    def countPermutations(self, complexity):
        n = len(complexity)

        c0 = complexity[0]
        for v in complexity[1:]:
            if v <= c0:
                return 0

        res = 1
        mod = MOD
        for x in range(1, n):
            res = (res * x) % mod

        return res
