class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        flag = 0
        result = []
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    result.append([nums[i],nums[l],nums[r]])
                    flag = 1
                    break
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        return result

# Test Program
nums = [1, -2, 1, 0, 5]
nums = [0, -1, 2, -3, 1]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]