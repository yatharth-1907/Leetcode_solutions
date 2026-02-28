class Solution:
    def intToRoman(self, num: int) -> str:
        symbol={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        value=0
        times=0
        res=''
        while num!=0:
            for i in symbol:
                if num-i>=0:
                    value=i
                    break
            times=num//value
            if times==0:
                res=res+symbol[value]
            for repeat in range(times):
                res=res+symbol[value]
            num=num%value
        return res


        
                

