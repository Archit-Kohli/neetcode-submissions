class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        out = 0 if len(s)==0 else 1
        curSeen = set()
        while r<len(s):
            while s[r] in curSeen:
                curSeen.remove(s[l])
                l+=1
            out = max(out,r-l+1)
            curSeen.add(s[r])
            r+=1
        return out
                        
