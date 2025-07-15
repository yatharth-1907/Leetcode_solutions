class Solution:
    def isValid(self, word: str) -> bool:
        vowel=0
        consonent=0
        other=0
        
        if len(word)>=3:
            for i in word:
                if i.isalpha():
                    if i.lower() in ['a','e','i','o','u']:
                        vowel+=1
                    else:
                        consonent+=1
                    
                elif i in ['@','#','$']:
                    other+=1
        if vowel and consonent and not other:
            return True
        else: 
            return False