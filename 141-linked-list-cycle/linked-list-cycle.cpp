/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* i= head;
        ListNode* j=head;
        if( i== NULL){
            return false;
        }

        while(j!= NULL && j->next!= NULL){

            i= i->next;
            j= j->next->next;
            if( i==j) 
            return true;

        }
        return false;
    }
};