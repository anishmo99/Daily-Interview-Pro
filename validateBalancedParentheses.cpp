#include <iostream>
#include <stack>
using namespace std;

bool validateBalancedParentheses(string str)
{
    stack<char>s;
    char c;
    for(int i=0;i<str.length();i++)
    {
        if(str.at(i)=='('||str.at(i)=='{'||str.at(i)=='[')
        {
            s.push(str.at(i));
            continue;
        }
        if(s.empty())
            return false;
        else
        {
            switch(str.at(i))
            {
                case ')':
                    c=s.top();
                    s.pop();
                    if(c=='{'||c=='[')
                        return false;
                    
                    break;
                case '}':
                    c=s.top();
                    s.pop();
                    if(c=='('||c=='[')
                        return false;
                    
                    break;
                case ']':
                    c=s.top();
                    s.pop();
                    if(c=='('||c=='{')
                        return false;
                
                    break;
            }
        }
    }
     return s.empty();
}

int main()
{
    int cases;
    cin>>cases;
    while(cases--)
    {
        string s;
        cin>>s;
        if(validateBalancedParentheses(s))
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
}
