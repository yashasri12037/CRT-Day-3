class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        freq = {}
        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in s2:
            freq[ch] = freq.get(ch, 0) - 1
        for count in freq.values():
            if count != 0:
                return False
        return True
