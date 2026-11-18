class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for st in strs:
            encoded+=str(len(st))+'#'+st
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        out = []
        while i < len(s):
            num = ''
            while s[i].isalnum() and s[i]!='#':
                num+=s[i]
                i+=1
            out.append(s[i+1:i+1+int(num)])
            i = i+1+int(num)
        return out