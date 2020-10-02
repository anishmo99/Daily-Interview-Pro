// USING SWAP WITH DFS (optimal backtracking)

class Solution
{
    vector<vector<int>> result;

public:
    void dfs(vector<int> &nums, int start)
    {
        if (start == nums.size() - 1)
        {
            result.emplace_back(nums);
            return;
        }
        for (int i = start; i < nums.size(); i++)
        {
            swap(nums[i], nums[start]);
            dfs(nums, start + 1);
            swap(nums[i], nums[start]);
        }
    }

    vector<vector<int>> permute(vector<int> &nums)
    {

        dfs(nums, 0);

        return result;
    }
};

// OR USING EXTRA VECTOR

class Solution
{
public:
    vector<vector<int>> permute(vector<int> &nums)
    {
        vector<vector<int>> result;

        vector<int> temp;
        // sort(nums.begin(), nums.end());

        func(nums, result, temp);

        return result;
    }

    void func(vector<int> &nums, vector<vector<int>> &result, vector<int> temp)
    {
        if (temp.size() == nums.size())
            result.emplace_back(temp);
        else
        {
            for (int i = 0; i < nums.size(); i++)
            {
                if (find(temp.begin(), temp.end(), nums[i]) != temp.end())
                    continue;
                temp.push_back(nums[i]);
                func(nums, result, temp);
                temp.pop_back();
            }
        }
    }
};