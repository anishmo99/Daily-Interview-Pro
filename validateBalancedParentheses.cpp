#include <iostream>
#include <stack>
using namespace std;

bool validateBalancedParentheses(string str)
{
    stack<char>s;
    for(int i=0;i<str.length();i++)
    {
        if(str.at(i)=='('||str.at(i)=='{'||str.at(i)=='[')
        {
            s.push(str.at(i));
            continue;
        }
        else
        {
            switch(str.at(i))
            {
                case ')':
                    if(s.top()=='{'||s.top()=='[')
                        return false;
                    s.pop();
                    break;
                case '}':
                    if(s.top()=='('||s.top()=='[')
                        return false;
                    s.pop();
                    break;
                case ']':
                    if(s.top()=='('||s.top()=='{')
                        return false;
                    s.pop();
                    break;
            }
        }
    }
     return s.empty();
}

int main()
{
    string s;
    getline(cin,s);
    cout<<validateBalancedParentheses(s)<<endl;
}
