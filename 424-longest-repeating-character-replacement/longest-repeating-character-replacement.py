class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = 0
        max_freq = 0
        max_ss = 0
        hashmap = {}
        i = 0
        j = i

        while j < len(s):
            if s[j] not in hashmap:
                hashmap[s[j]] = 1
                max_freq = max(max_freq, hashmap[s[j]])
                size += 1
            else:
                hashmap[s[j]] += 1
                max_freq = max(hashmap.values())
                size += 1

            if k >= size - max_freq:
                max_ss = max(max_ss, size)
                j += 1
            else:
                hashmap[s[i]] -= 1
                i += 1
                size -= 1
                j += 1

        return max_ss