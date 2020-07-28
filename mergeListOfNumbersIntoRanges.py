def findRanges(nums):
    sol = []
    if len(nums) == 0 or len(nums) == 1:
        return nums
    
    # temp = nums
    
    # [temp.append(x) for x in nums if x not in temp]
    
    i,j = 0,1
    prev, cur = nums[i],nums[j]
    
    while j < len(nums):
        if prev+1 == cur or prev == cur:
           prev = cur 
        else:
            sol.append([nums[i],prev])
            i = j
            prev = cur
        j += 1
        if j < len(nums):
            cur = nums[j]
    
    sol.append([nums[i],prev])
    
    return sol

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']