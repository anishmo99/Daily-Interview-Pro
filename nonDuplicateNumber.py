def nonDuplicateNumber(nums):
    nums.sort()
    i=0
    while(i<len(nums)-1):
        if nums[i]!=nums[i+1]:
            return nums[i]
        i+=2
    return nums[len(nums)-1]

print nonDuplicateNumber([4, 3, 3, 2, 1, 2, 1])
# 1
