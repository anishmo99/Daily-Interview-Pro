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
class Solution
{
public:
    ListNode *removeZeroSumSublists(ListNode *head)
    {
        ListNode *dummy = new ListNode(0);

        map<int, ListNode *> map;

        map[0] = dummy;
        dummy->next = head;

        ListNode *ptr = head;

        int sum = 0;
        while (ptr)
        {
            sum += ptr->val;
            if (map.find(sum) != map.end())
            {
                ListNode *ptr2 = map[sum];

                int cur_sum = sum;
                while (ptr2 and ptr2 != ptr)
                {
                    ptr2 = ptr2->next;
                    cur_sum += ptr2->val;
                    if (ptr2 != ptr)
                        map.erase(cur_sum);
                }
                map[sum]->next = ptr->next;
            }
            else
            {
                map[sum] = ptr;
            }
            ptr = ptr->next;
        }

        return dummy->next;
    }
};