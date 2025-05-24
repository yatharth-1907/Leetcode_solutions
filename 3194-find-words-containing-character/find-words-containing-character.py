class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output=[]
        for index in range(len(words)):
            if (x in words[index]):
                output.append(index)
        return output