class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        for str1 in strs:
            repr="".join(sorted(str1,key=lambda x:x))
            groups[repr].append(str1)
        return list(groups.values())
        