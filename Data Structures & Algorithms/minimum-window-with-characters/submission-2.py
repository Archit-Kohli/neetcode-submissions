class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        minLength = len(s) + 1
        out = ""
        thmap = defaultdict(int)
        for ch in t:
            thmap[ch] += 1
        shmap = defaultdict(int)
        have, need = 0, len(thmap)
        i = 0
        for j in range(len(s)):
            ch = s[j]
            shmap[ch] += 1
            if ch in thmap and shmap[ch] == thmap[ch]:
                have += 1
            while have == need:
                if j - i + 1 < minLength:
                    minLength = j-i+1
                    out = s[i:j+1]
                left_ch = s[i]
                shmap[left_ch] -= 1
                if left_ch in thmap and shmap[left_ch] < thmap[left_ch]:
                    have -= 1
                i += 1
        return out