class Solution
{
public:
    int numIslands(vector<vector<char>> &grid)
    {
        int islands = 0;
        int dir[] = {0, 1, 0, -1, 0};
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {
                if (grid[i][j] == '1')
                {
                    grid[i][j] = '0';
                    islands++;
                    queue<pair<int, int>> q;
                    q.push({i, j});
                    while (!q.empty())
                    {
                        pair<int, int> temp = q.front();
                        q.pop();
                        for (int k = 0; k < 4; k++)
                        {
                            int x = temp.first + dir[k];
                            int y = temp.second + dir[k + 1];
                            if (x < grid.size() and x >= 0 and y < grid[0].size() and y >= 0 and grid[x][y] == '1')
                            {
                                q.push({x, y});
                                grid[x][y] = '0';
                            }
                        }
                    }
                }
            }
        }
        return islands;
    }
};