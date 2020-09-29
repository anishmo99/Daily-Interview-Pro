class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ump1, ump2 = dict(), dict()
        
        for i in range(len(s)):
            if s[i] in ump1 and ump1[s[i]] != t[i]:
                return False
            ump1[s[i]] = t[i]
            
        for i in range(len(t)):
            if t[i] in ump2 and ump2[t[i]] != s[i]:
                return False
            ump2[t[i]] = s[i]
            
        return True