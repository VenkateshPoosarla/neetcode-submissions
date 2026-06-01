class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen=0
        set1=set(nums)
        for i in range(len(nums)):
            if nums[i]-1 not in set1:
                count=1
                temp=nums[i]+1
                while temp in set1:
                    count +=1
                    temp +=1
                maxLen=max(count,maxLen)
        return maxLen