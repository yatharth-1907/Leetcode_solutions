class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        operation=[]
        idx=k-1
        if idx<2:operation=[0]
        else:
            lg= int(math.log2(idx))
            while lg>0:
                if idx==0:
                    lg=0
                else:lg= int(math.log2(idx))
                rem= idx% 2**lg
                operation.append(lg)
                idx=rem
                if idx==0:
                    break
        ch='a'
        if k>1:
            for i in operation[::-1]:
                if operations[i]:
                    if (ord(ch)+1)<123:
                        ch= chr((ord(ch)+1))
                    else:
                        ch= chr((ord(ch)+1)%123+97)

        return ch
                    