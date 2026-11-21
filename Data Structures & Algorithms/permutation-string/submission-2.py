class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hmap1 = [0]*26
        for i in range(len(s1)):
            hmap1[ord(s1[i])-ord('a')] += 1
        window = len(s1)
        hmap2 = [0]*26
        for i in range(len(s1)):
            hmap2[ord(s2[i])-ord('a')] += 1
        if hmap2 == hmap1:
            return True
        for i in range(1,len(s2)-window+1):
            hmap2[ord(s2[i-1])-ord('a')]-=1
            hmap2[ord(s2[i+window-1])-ord('a')]+=1
            if hmap2 == hmap1:
                return True
        return False