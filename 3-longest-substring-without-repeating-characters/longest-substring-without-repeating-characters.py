class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        n=len(s)
        result=[]
        longest=0
        while left<n and right<n:
            if s[right] not in result:
                result.append(s[right])
            else:
                index= result.index(s[right])
                result= result[index+1:]
                result.append(s[right])
                left=left+index+1
            longest=max(longest, right-left+1)
            right+=1
        return longest

