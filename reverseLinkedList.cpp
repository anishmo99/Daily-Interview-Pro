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

