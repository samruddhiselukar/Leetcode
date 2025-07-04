class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = -1
        sum = 0 
        total_sum = 0

        for i in nums:
            total_sum += i

        for i in range(len(nums)):
            # initially  sum remains 0 here and pivot is set to 1st ele
            pivot = nums[i] 

            # we make a check if the sum to both sides of the pivot is same
            if sum == total_sum - nums[i] - sum: 
                # if it is we return the index
                return i 
            
            # otherwise we add the current ele to the sum and move to next ele considering the next element as pivot
            sum += nums[i] 

        # result is returned in any case
        return res
