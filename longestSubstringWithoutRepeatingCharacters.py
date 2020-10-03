class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, max_len = 0, 0, 0
        
        hash_set = set()
        
        while j < len(s):
            if s[j] not in hash_set:
                hash_set.add(s[j])
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                hash_set.remove(s[i])
                i += 1
                
        return max_len
        