class Solution
{
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix)
    {
        vector<int> vec;

        if (matrix.empty())
            return vec;

        int top = 0, down = matrix.size() - 1, left = 0, right = matrix[0].size() - 1;
        int dir = 0;

        while (top <= down and left <= right)
        {
            if (dir == 0)
            {
                for (int i = left; i <= right; i++)
                {
                    vec.push_back(matrix[top][i]);
                }
                top++;
            }
            else if (dir == 1)
            {
                for (int i = top; i <= down; i++)
                {
                    vec.push_back(matrix[i][right]);
                }
                right--;
            }
            else if (dir == 2)
            {
                for (int i = right; i >= left; i--)
                {
                    vec.push_back(matrix[down][i]);
                }
                down--;
            }
            else
            {
                for (int i = down; i >= top; i--)
                {
                    vec.push_back(matrix[i][left]);
                }
                left++;
            }
            dir = (dir + 1) % 4;
        }

        return vec;
    }
};