#include <iostream>
#include <stack>
using namespace std;

string reverseWords(string s)
{
    string result;
    stack<char> stack;
    for(int i=0;i<s.length();i++)
    {
        if(s[i]!=' ')
        {
            stack.push(s[i]);
        }
        else
        {
            while(!stack.empty())
            {
                result.push_back(stack.top());
                stack.pop();
            }
            result.push_back(' ');
        }
    }
    while(!stack.empty())
    {
        result.push_back(stack.top());
        stack.pop();
    }
    return result;
}

int main()
{
    string s;
    getline(cin,s);
    string result = reverseWords(s);
    cout<<result;
}