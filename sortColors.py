class Solution:
  def sortColors(self, nums):
    count_0 = count_1 = count_2 = 0
    
    for i in nums:
        if i==0:
            count_0+=1
        elif i==1:
            count_1+=1
        elif i==2:
            count_2+=1
     
    i=0
    while count_0>0:
        nums[i]=0
        i+=1
        count_0-=1

    while count_1>0:
            nums[i]=1
            i+=1
            count_1-=1

    while count_2>0:
            nums[i]=2
            i+=1
            count_2-=1



nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]