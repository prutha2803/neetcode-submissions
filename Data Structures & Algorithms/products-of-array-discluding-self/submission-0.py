class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        left= [1]*n
        for i in range(1, n):
            left[i]= nums[i-1]* left[i-1]

        right=1
        for i in range(n-1, -1,-1):
            left[i]*=right
            right*= nums[i]
        
        return left

        