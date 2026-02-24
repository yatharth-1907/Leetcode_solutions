class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter=[]
        for i in s:
            if i.isalnum():
                letter.append(i.lower())
        return letter == letter[::-1]
