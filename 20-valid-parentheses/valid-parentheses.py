class Solution:
    def isValid(self, s: str) -> bool:
        list=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                list.append(i)
            elif not list:
                return False
            else:
                if list[len(list)-1]=="(" and i==")":
                    list.pop()
                elif list[len(list)-1]=="[" and i=="]":
                    list.pop()
                elif list[len(list)-1]=="{" and i=="}":
                    list.pop()
                else:
                    return False
        if not list:
            return True
        return False