from collections import defaultdict
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashmap = defaultdict(int)
        length = 0
        central_used = False

        for word in words:
            hashmap[word] += 1

        for word in list(hashmap.keys()):
            rev = word[::-1]
            if word != rev:
                if rev in hashmap:
                    pairs = min(hashmap[word], hashmap[rev])
                    length += 4 * pairs  
                    hashmap[word] -= pairs
                    hashmap[rev] -= pairs
            else:
                pairs = hashmap[word] // 2
                length += 4 * pairs
                hashmap[word] -= 2 * pairs
                if hashmap[word] > 0 and not central_used:
                    length += 2
                    central_used = True

        return length
