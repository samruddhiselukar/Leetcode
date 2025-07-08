# 2 pointer
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0

        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else: 
                return 1

        l, r = 0, len(nums) - 1
        k = 0
        while l <= r:
            while nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                nums[r] = '_'
                r -= 1
                k += 1
            else:
                l += 1
        return len(nums) - k 
            
        

