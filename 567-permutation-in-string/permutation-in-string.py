class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        i=0
        j=len(s1)-1
        while j<len(s2):
            per= sorted(s2[i:j+1])
            if per==s1:
                return True 
            i+=1
            j+=1
        return False