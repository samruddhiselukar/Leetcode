class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = res ^ nums[i] # a ^ a = 0 and a ^ 0 = a

        return res
