// Input : [ 10, 9, 2, 5, 3, 7, 101, 18 ]
// Output : 4
// Explanation : The longest increasing subsequence is [2, 3, 7, 101],
// therefore the length is 4.

// Note:

// There may be more than one LIS combination,
// It is only necessary for you to return the length.
// Your algorithm should run in O(n2) complexity.

// o(n^2) 

class Solution
{
public:
    int lengthOfLIS(vector<int> &nums)
    {
        if (nums.empty())
            return 0;
        vector<int> dp(nums.size(), 1);
        for (int i = 1; i < nums.size(); i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (nums[j] < nums[i] and dp[i] < dp[j] + 1)
                    dp[i]++;
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};