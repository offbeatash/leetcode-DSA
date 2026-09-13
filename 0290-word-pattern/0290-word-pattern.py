class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern)!= len(words):
            return False

        p_w ={}
        w_p ={}

        for p,w in zip(pattern,words):

            if p in p_w and p_w[p] != w:
                return False
            
            if w in w_p and w_p[w] != p:
                return False
            
            p_w[p] = w
            w_p[w] = p
            
        return True