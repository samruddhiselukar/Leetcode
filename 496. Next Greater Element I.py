# O(n x m) solution
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Map = { n : i for i, n in enumerate(nums1)} 
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in nums1Map:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    res[nums1Map[nums2[i]]] = nums2[j]
                    break
        return res
