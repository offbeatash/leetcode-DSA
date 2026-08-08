class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        count = [0] * 26

        for c in magazine:
            count[ord(c) - 97] += 1

        for c in ransomNote:
            i = ord(c) - 97
            count[i] -= 1
            if count[i] < 0:
                return False

        return True