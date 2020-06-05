#include <cstring>
#include <iostream>
using namespace std;

string longestPalindromicSubstring(string s)
{
    if(s.empty()||s=="")
        return "";
    
    int len=s.length();
    int start=0,maxlength=1;
    
    bool dp[n][n];
    memset(dp,0,sizeof(dp));
    
    for(int i=0;i<len;i++)
        dp[i][i]=true;
    
    for(int i=0;i<len-1;i++)
        if(s[i]==s[i+1])
        {
            dp[i][i+1]=true;
            start = i;
            maxlength=2;
        }
    
    for(int k=3;k<=len;k++)
    {
        for(int i=0;i<=len-k;i++)
        {
            int j=i+k-1;
            if(s[i]==s[j]&&dp[i+1][j-1])
            {
                dp[i][j]=true;
                if(maxlength<k)
                {
                    start=i;
                    maxlength=k;
                }
            }
        }
    }
    return s.substr(start,maxlength);
}

int main()
{
    int cases;
    cin>>cases;
    while(cases--)
    {
        string str;
        cin>>str;
        cout<<longestPalindromicSubstring(str)<<endl;
    }
    return 0;
}
