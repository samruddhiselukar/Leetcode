class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        pre, post = 1, 1
        for i in range(len(nums)):
            # nums = [1, 2, 3, 4]
            # res = [1, 1, 2, 6]
            res[i] = pre 
            pre = pre * nums[i]
        
        for i in range(len(nums) -1, -1, -1):
            # nums = [1, 2, 3, 4]
            # res = [24, 12, 8, 6]
            res[i] = post * res[i] 
            post *= nums[i] # post = 24

        return res


