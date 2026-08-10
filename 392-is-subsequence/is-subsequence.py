class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s.strip() =="":
            return True
        idx= 0
        for i in t:
            if s[idx]==i:
                idx+=1
                if idx >=len(s):
                    return True
        return False
