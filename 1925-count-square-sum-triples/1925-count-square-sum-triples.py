class Solution:
    def countTriples(self, n: int) -> int:
        squares = {i*i for i in range(1, n+1)}
        res = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                if a*a + b*b in squares:
                    res += 1
        return res
