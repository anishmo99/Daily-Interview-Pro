# Solutions

 <ol>
<li>
	<div>
	 Reverse a Linked List: 
	 <ul>
	  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/reverseLinkedList.py">Python</a></li>

~~~python
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  
  # Function to print the list
  def printList(self):
    node = self
    output = ''
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):
    cur = head
    prev = None
    while cur is not None:
        next=cur.next
        cur.next=prev
        prev=cur
        cur=next
    self.head=prev

  # Recursive Solution
#  def reverseRecursively(self, head):
    # Implement this.

# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
#testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
~~~
<li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/reverseLinkedList.cpp">CPP</a></li></ul>

~~~cpp
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};

Node* reverseList(Node *head)
{
  struct Node *cur=head,*prev=NULL,*next=NULL;
  while(cur!=NULL)
  {
      next=cur->next;
      cur->next=prev;
      prev=cur;
      cur=next;
  }
  head=prev;
  return head;
}

~~~

</div>
</li>
<li>
	<div>
	 Validate Balanced Parentheses: 
	 <ul>
	  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/validateBalancedParentheses.py">Python</a></li>

~~~python
def validateBalancedParentheses(str):
    stack=[]
    for i in str:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
        else:
            if len(stack)==0: return False
            if i==')':
                if stack[len(stack)-1]=='{' or stack[len(stack)-1]=='[':
                    return False
#                stack.pop()
            if i=='}':
                if stack[len(stack)-1]=='(' or stack[len(stack)-1]=='[':
                    return False
#                stack.pop()
            if i==']':
                if stack[len(stack)-1]=='{' or stack[len(stack)-1]==')':
                    return False
            stack.pop()
    return True if len(stack)==0 else False
str=input()
print(validateBalancedParentheses(str))
~~~

  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/validateBalancedParentheses.cpp">CPP</a></li></ul>

~~~cpp
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
~~~

</div>
</li>
<li>
	<div>
	Sort a List with 3 Unique Numbers: 
	 <ul>
	  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/sort3UniqueNumbers.py">Python</a></li>

~~~python
def sortNums(nums):
    c1,c2,c3=0,0,0
    for i in nums:
        if i==1:
            c1+=1
        elif i==2:
            c2+=1
        else:
            c3+=1
    l1=c1*[1]+c2*[2]+c3*[3]
    return l1

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
~~~

  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/sort3UniqueNumbers.cpp">CPP</a></li></ul>

~~~cpp
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
~~~

</div>
</li>
<li>
	<div>
	First and Last Indices of an Element in a Sorted Array: 
	 <ul>
	  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/firstAndLastIndicesOfElementInSortedArray.py">Python</a></li>

~~~python
class Solution:
  def getRange(self, arr, target):
    if target not in arr:
        return -1
    first=0
    last=0
    flag=0
    for i in range(len(arr)):
        if arr[i]==target and flag==0:
            flag=1
            first=i
            last=i
        elif arr[i]==target and flag==1:
            last=i
    return [first,last]
        
        
            
    
# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
~~~

  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/firstAndLastIndicesOfElementInSortedArray.cpp">CPP</a></li></ul>

~~~cpp
#include <iostream>
using namespace std;

void findRange(int arr[],int n,int target)
{
    int first,second,flag=0;
    for(int i{};i<n;i++)
    {
        if(arr[i]==target&&flag==0)
        {
            flag=1;
            first=i;
            second=i;
        }
        else if(arr[i]==target&&flag==1)
        {
            second=i;
        }
    }
    if(flag==0)
    {
        cout<<-1;
        return;
    }
    cout<<first<<" "<<second;
}

int main() {
    int cases;
    cin>>cases;
    while(cases--)
    {
        int target;
        int n;
        cin>>n>>target;
        int arr[n];
        for(int i{};i<n;i++)
            cin>>arr[i];
        findRange(arr,n,target);
        cout<<endl;
    }
    return 0;
}
~~~

</div>
</li>
<li>
    <div>
    Two Sum: 
     <ul>
      <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/twoSum.py">Python</a></li>

~~~python
def two_sum(list, target):
    s=set()
    for i in list:
        if target-i in s:
            return True
        s.add(i)
    return False
    

print(two_sum([4,7,1,-3,2], 5)) #True
print(two_sum([4,7,1,-3,2],10)) #False
~~~
  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/twoSum.cpp">CPP</a></li>

~~~cpp
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
~~~
</ul>
</div>
</li>
</ol>
