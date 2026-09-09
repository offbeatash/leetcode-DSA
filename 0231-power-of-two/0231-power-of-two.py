class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and  (n &(n-1)) == 0

#using bitwise and(&) operator.
#n must be +ve, and power of 2 has only '1' in binary.
#n &(n-1) removes that '1', so result becomes 0, means power of 2.