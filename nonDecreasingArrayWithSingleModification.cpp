class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int p = -1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i-1] > nums[i]) {
                if (p != -1) return false;
                else p = i;
            }
        }
        return ( p == -1 || p == 1 || p == nums.size() - 1 || nums[p - 2] <= nums[p] || nums[p - 1] <= nums[p + 1]);
    }
};

