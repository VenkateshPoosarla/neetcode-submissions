class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(s,key=lambda x:x)) == "".join(sorted(t,key=lambda x:x))
        