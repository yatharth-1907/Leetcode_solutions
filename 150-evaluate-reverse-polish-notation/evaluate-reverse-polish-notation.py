class Solution:
    def operation (self,n1,n2, op):
        if op=='+':
            return n1+n2
        elif op=='-':
            return n2-n1
        elif op=='*':
            return n1*n2
        elif op=='/':
            return int(n2/n1)
        else:
            return 0
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operants=['+','-','*','/']
        for i in tokens:
            if i in operants:
                res= self.operation(stack.pop(), stack.pop(),i)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack.pop()

