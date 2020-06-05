# Daily Interview Pro
 Questions solved in Python and CPP from Daily-Interview-Pro
 <ol>
<li>
	<div>
	 Reverse a Linked List: 
	 <ul>
	  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/reverseLinkedList.py">Python</a></li>
	  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/reverseLinkedList.cpp">CPP</a></li></ul>
	</div>
</li>
<li>
	<div>
	 Validate Balanced Parentheses: 
	 <ul>
	  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/validateBalancedParentheses.py">Python</a></li>
	  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/validateBalancedParentheses.cpp">CPP</a></li></ul>
	</div>
</li>
<li>
	<div>
	Sort a List with 3 Unique Numbers: 
	 <ul>
	  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/sort3UniqueNumbers.py">Python</a></li>
	  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/sort3UniqueNumbers.cpp">CPP</a></li></ul>
	</div>
</li>
<li>
	<div>
	First and Last Indices of an Element in a Sorted Array: 
	 <ul>
	  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/firstAndLastIndicesOfElementInSortedArray.py">Python</a></li>
	  <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/firstAndLastIndicesOfElementInSortedArray.cpp">CPP</a></li></ul>
	</div>
</li>
<li>
    <div>
    Two Sum: 
     <ul>
      <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/twoSum.py">Python</a></li>
      <li><a href="https://github.com/anishmo99/DailyInterviewPro/blob/master/twoSum.cpp">CPP</a></li>

```cpp
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
```
</ul>
</div>
</li>
</ol>
