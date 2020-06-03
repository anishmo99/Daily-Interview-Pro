class Solution:
  def getRange(self, arr, target):
    if target not in arr:
        return -1
    first=0
    last=0
    flag=0
    for i in range(len(arr)):
        if arr[i]==target and flag==0:
            flag=1
            first=i
            last=i
        elif arr[i]==target and flag==1:
            last=i
    return [first,last]
        
        
            
    
# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
