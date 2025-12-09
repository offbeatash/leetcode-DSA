MOD = 10**9 + 7

class Solution:
    def specialTriplets(self, nums):
        prev_freq = {}
        next_freq = {}

        for x in nums:
            next_freq[x] = next_freq.get(x, 0) + 1

        ans = 0
        for num in nums:
            next_freq[num] -= 1

            target = 2 * num
            left = prev_freq.get(target, 0)
            right = next_freq.get(target, 0)
            ans += left * right

            prev_freq[num] = prev_freq.get(num, 0) + 1

        return ans % MOD
