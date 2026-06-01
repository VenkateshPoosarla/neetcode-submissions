class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        out=sorted(nums,key=lambda x:x)
        for i in range(1,len(nums),1):
            if out[i-1]==out[i]:
                return True
        return False
        