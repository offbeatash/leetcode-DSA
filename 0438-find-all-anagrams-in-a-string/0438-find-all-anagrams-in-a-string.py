class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        count = [0]*26

        for ch in p:
            count[ord(ch)-97] +=1
            
        for ch in s[:len(p)]:
            count[ord(ch)-97] -=1

        result = []

        if all(x==0 for x in count):
            result.append(0)

        for i in range(len(p), len(s)):
            count[ord(s[i])-97] -=1
            count[ord(s[i - len(p)])-97] +=1

            if all(x ==0 for x in count):
                result.append(i-len(p) + 1)

        return result