class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        count = [0] * 26

        for ch in p:
            count[ord(ch) - 97] += 1

        for ch in s[:len(p)]:
            count[ord(ch) - 97] -= 1

        result = []

        diff = sum(x != 0 for x in count)

        if diff == 0:
            result.append(0)

        for i in range(len(p), len(s)):
            idx = ord(s[i]) - 97

            if count[idx] == 0:
                diff += 1
            count[idx] -= 1
            if count[idx] == 0:
                diff -= 1

            idx = ord(s[i - len(p)]) - 97

            if count[idx] == 0:
                diff += 1
            count[idx] += 1
            if count[idx] == 0:
                diff -= 1

            if diff == 0:
                result.append(i - len(p) + 1)

        return result