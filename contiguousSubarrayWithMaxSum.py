class Solution:
    def maxSubArraySum(self, arr: List[int]) -> int:
        cur_sum,max_sum=arr[0],arr[0]
        for i in range(1,len(arr)):
            cur_sum = max(arr[i],arr[i]+cur_sum)
            max_sum = max(cur_sum,max_sum)
        return max_sum