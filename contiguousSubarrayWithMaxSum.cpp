class Solution
{
public:
    int maxSubArray(vector<int> &arr)
    {
        int cur_sum, max_sum;
        cur_sum = max_sum = arr[0];
        for (int i = 1; i < arr.size(); i++)
        {
            cur_sum = max(arr[i], cur_sum + arr[i]);
            max_sum = max(cur_sum, max_sum);
        }
        return max_sum;
    }
};