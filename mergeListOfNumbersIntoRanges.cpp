#include <iostream>
#include <vector>

using namespace std;

vector<pair<int,int> > findRanges(vector<int> nums)
{
    vector<pair<int,int> > result;
    
    if(nums.size() == 0 or nums.size() == 1)
        return result;
    
    int i = 0, j = 1;
    int prev = nums[i], cur = nums[j];

    while(j < nums.size())
    {
        if(prev + 1 == cur or prev == cur)
            prev = cur;
        else
        {
            result.emplace_back(nums[i],prev);
            i = j;
            prev = cur;
        }
        j++;
        if(j < nums.size())
            cur = nums[j];
    }
    result.emplace_back(nums[i],prev);
    return result;
}

int main()
{
    int n;
    cin>>n;
    vector<int> arr(n);
    for(int i=0;i<n;i++)
        cin>>arr[i];
    vector<pair<int,int> > sol = findRanges(arr);
    for(auto x : sol)
    {
        cout<<x.first<<", "<<x.second<<endl;
    }
    return 0;
}