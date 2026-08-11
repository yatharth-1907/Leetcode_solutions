class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count=0
        current= word
        while current in sequence:
            current+=word
            count+=1
        return count