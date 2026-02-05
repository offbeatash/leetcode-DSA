class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        first = strs[0]
        
        for i in range(len(first)):
            ch = first[i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != ch:
                    return first[:i]
        
        return first
