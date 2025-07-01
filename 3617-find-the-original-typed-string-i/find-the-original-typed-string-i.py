class Solution:
    def possibleStringCount(self, word: str) -> int:
        count=0
        length= len(word)
        for i in range(length-1):
            if word[i]!= word[i+1]:
                count+=1
    
        return length-count