class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [x for x in nums1 if x in nums2]
        return set(result)

# better solution

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = set(nums1)
        result = []
        for i in nums2:
            if i in common:
                result.append(i)
                common.remove(i)
        return result