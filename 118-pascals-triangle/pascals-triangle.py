class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def rowGenerator(row):
            temp=[1]
            ans=1
            for i in range(1,row):
                ans=ans*(row-i)
                ans=ans/i
                temp.append(int(ans))
            return temp
        
        tri=[]
        for i in range(1,numRows+1):
            tri.append(rowGenerator(i))
        return tri