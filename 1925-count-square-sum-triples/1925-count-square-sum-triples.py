import math

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        # Generate primitive triples via Euclid's formula
        # a = m^2 - n^2, b = 2mn, c = m^2 + n^2
        m_max = int(math.isqrt(n))  # since c = m^2 + n^2 <= n
        for m in range(2, m_max + 1):
            for nn in range(1, m):
                if ((m - nn) % 2 == 1) and math.gcd(m, nn) == 1:
                    a = m*m - nn*nn
                    b = 2*m*nn
                    c = m*m + nn*nn
                    if c > n:
                        continue
                    # Scale primitive triple by k while staying within bounds
                    k_max = n // c
                    for k in range(1, k_max + 1):
                        ak, bk, ck = k*a, k*b, k*c
                        if ak <= n and bk <= n and ck <= n:
                            # Count ordered pairs (a,b,c) and (b,a,c)
                            res += 2 if ak != bk else 1
        return res
