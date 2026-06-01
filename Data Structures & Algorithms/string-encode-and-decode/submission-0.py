class Solution:

    def encode(self, strs: List[str]) -> str:
        out=""
        for str1 in strs:
            out =out+f"{len(str1)}:{str1}"
        return out

    def decode(self, s: str) -> List[str]:
        pos=0
        out=[]
        while pos<len(s):
            newpos=s.index(":",pos)
            size=int(s[pos:newpos])
            s1=s[newpos+1:newpos+size+1]
            out.append(s1)
            pos=newpos+1+size
        return out
