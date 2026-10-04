class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(s, open, close):
            if open == n and close == n:
                ans.append(s)
                return
            
            if open < n:
                backtrack(s + '(', open+1, close)

            if close < open :
                backtrack(s + ')', open, close+1)

        backtrack("", 0,0)
        return ans