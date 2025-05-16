class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        Group=defaultdict(list)
        count=[0]*26
        for str in strs:
            count=[0]*26
            for char in str:
                count[ord(char)-ord('a')]+=1
            Group[tuple(count)].append(str)

        return Group.values()