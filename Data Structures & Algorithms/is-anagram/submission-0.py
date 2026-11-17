class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0]*26
        for i in s:
            counts[ord(i)-ord('a')]+=1
        for j in t:
            counts[ord(j)-ord('a')]-=1
        for x in counts:
            if x!=0:
                return False
        return True