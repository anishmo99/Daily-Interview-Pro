#include <iostream>
#include <set>
using namespace std;

bool twoSum(int arr[],int n,int target)
{
    set<int>hash_set;
    for(int i{};i<n;i++)
    {
        if(hash_set.find(target-arr[i])!=hash_set.end())
            return true;
        hash_set.insert(arr[i]);
    }
    return false;
}

int main()
{
    int n;
    cin>>n;
    int target;
    cin>>target;
    int arr[n];
    for(int i{};i<n;i++)
        cin>>arr[i];
    cout<<twoSum(arr,n,target)<<endl;
}
