class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_set<char> hash;

        int i = 0, j = 0, max_len = 0;

        while (j < s.size())
        {
            if (hash.find(s.at(j)) == hash.end())
            {
                hash.insert(s.at(j));
                max_len = max(max_len, j - i + 1);
                j++;
            }
            else
            {
                hash.erase(s.at(i));
                i++;
            }
        }

        return max_len;
    }
};