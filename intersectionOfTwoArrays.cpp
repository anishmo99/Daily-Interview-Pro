class Solution
{
public:
    vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
    {
        unordered_set<int> set1, set2;
        for (auto i : nums1)
            set1.insert(i);
        for (auto i : nums2)
        {
            if (set1.find(i) != set1.end())
                set2.emplace(i);
        }
        return {set2.begin(), set2.end()};
    }
};