#include <iostream>
#include <algorithm>
using namespace std;

int nonDuplicateNumber(int arr[],int n)
{
    sort(arr,arr+n);
    for(int i{};i<n-1;i++)
    {
        if(arr[i]!=arr[i+1])
            return arr[i];
        i++;
    }
    return arr[n-1];
}

int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
        cin>>arr[i];
    cout<<nonDuplicateNumber(arr,n)<<endl;
}
