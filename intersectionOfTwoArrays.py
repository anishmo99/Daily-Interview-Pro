class Solution:
    def intersection(self, nums1, nums2):
        result = [x for x in nums1 if x in nums2]
        return set(result)

# better solution

class Solution:
    def intersection(self, nums1, nums2):
        common = set(nums1)
        result = []
        for i in nums2:
            if i in common:
                result.append(i)
                common.remove(i)
        return result


print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))