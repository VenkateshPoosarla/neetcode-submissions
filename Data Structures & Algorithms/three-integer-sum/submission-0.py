class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l<r:
                if nums[l]+nums[r]== -nums[i]:
                    out.append([nums[i],nums[l],nums[r]])
                    l +=1
                    r -=1
                # Skip duplicate values for the second element
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # Skip duplicate values for the third element
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l]+nums[r] > -nums[i]:
                    r -=1
                else:
                    l +=1
        return out
        