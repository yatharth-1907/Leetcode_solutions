class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       s1_dict= [0]*26
       s2_dict= [0]*26
       for letter in s1:
           s1_dict[ord(letter)-ord('a')]+=1
       i=0
       j=0

       while j<len(s2):
           s2_dict[ord(s2[j])-ord('a')]+=1
           if j-i+1==len(s1):
               if s1_dict==s2_dict:
                   return True
               else:
                   s2_dict[ord(s2[i])-ord('a')]-=1
                   i+=1
           j+=1

       return False