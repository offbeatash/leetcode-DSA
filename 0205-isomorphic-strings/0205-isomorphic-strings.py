class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST ={}
        mapTS ={}

        for a,b in zip(s,t):
            if a in mapST and mapST[a] != b:
                return False
            if b in mapTS and mapTS[b] != a:
                return False
            
            mapST[a] =b
            mapTS[b] =a
        
        return True