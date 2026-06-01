class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left_prod=[1] * n
        right_prod=[1] * n
        left,right=1,1
        for i in range(len(nums)):
            left_prod[i]=left
            left *=nums[i]
            right_prod[n-i-1]=right
            right *=nums[n-i-1]
        return [left_prod[i]*right_prod[i] for i in range(len(nums))]

        