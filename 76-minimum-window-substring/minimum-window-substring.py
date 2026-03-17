class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)< len(t):
            return ""
        hmap={}
        for i in t:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i]=1

        reqCount= len(t)
        startIdx=None
        minWindow=float('inf')
        i=0
        j=0
        while j<len(s) and i<len(s):
            if s[j] in hmap:
                if  hmap[s[j]]>0:
                    reqCount-=1
                hmap[s[j]]-=1

            while reqCount==0:
                if minWindow>j-i+1:
                    minWindow=j-i+1
                    startIdx= i
                if s[i]in hmap:
                    hmap[s[i]]+=1
                    if hmap[s[i]]>0:
                        reqCount+=1
                i+=1
            j+=1

        return s[startIdx:startIdx+minWindow] if startIdx!=None else ""
                