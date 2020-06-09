#include <iostream>
using namespace std;

struct Node {
    int data;
    struct Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

Node* addTwoLists(Node* A, Node* B){
    if(!A)
        return B;
    if(!B)
        return A;
    
    int sum=0,carry=0;
    sum=A->data+B->data+carry;
    Node* newHeadTraverse=new Node(sum%10);
    carry=sum/10;
    Node* newHeadPtr=newHeadTraverse;
    A=A->next;
    B=B->next;
    while(A||B||carry)
    {
        sum=(A?A->data:0)+(B?B->data:0)+carry;
        Node* temp=new Node(sum%10);
        carry=sum/10;
        newHeadTraverse->next=temp;
        newHeadTraverse=newHeadTraverse->next;
        if(A)
            A=A->next;
        if(B)
            B=B->next;
    }
    return newHeadPtr;
}
