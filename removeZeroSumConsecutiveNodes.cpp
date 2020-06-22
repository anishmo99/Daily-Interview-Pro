/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        if(head==NULL){
            return NULL;
        }
        ListNode* dummy=new ListNode(0);
        map<int,ListNode*>m;
        dummy->next=head;
    m[0]=dummy;
         
        ListNode*temp=head;
        int prevsum=0;
        while(temp!=NULL){
            prevsum+=temp->val;
            if(m.find(prevsum)!=m.end()){
                int sum=prevsum;
                ListNode*temp2=m[prevsum];
                while(temp2!=NULL&&temp2!=temp){
                    temp2=temp2->next;
                    sum+=temp2->val;
                    if(temp2!=temp){
                        m.erase(sum);
                    }
                }
                m[prevsum]->next=temp->next;
            }
            else{
                m[prevsum]=temp;
            }
            temp=temp->next;
            
        }
        return dummy->next;}
};
