#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int>vec{3, 3, 2, 1, 3, 2, 1};
    int c1,c2,c3;
    c1=c2=c3=0;
    for(int i:vec)
    {
        if(i==1)
            c1++;
        if(i==2)
            c2++;
        if(i==3)
            c3++;
    }
    int i=0;
    while(c1--)
    {
        vec[i++]=1;
    }
    while(c2--)
    {
        vec[i++]=2;
    }
    while(c3--)
    {
        vec[i++]=3;
    }
    for(int i:vec)
        cout<<i<<" ";
}
