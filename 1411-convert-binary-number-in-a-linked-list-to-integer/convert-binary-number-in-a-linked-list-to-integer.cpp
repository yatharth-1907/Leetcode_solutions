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
    int getDecimalValue(ListNode* head) {
        ListNode *ptr= head;
        vector<int> binary={};
        
        while (ptr!= NULL) {
            binary.push_back(ptr->val);
            ptr= ptr->next;
        }

        int power=0;
        int decimal=0;
        for (int i= binary.size()-1;i>=0; i--){
            decimal= decimal+(pow(2,power)*binary[i]);
            power++;
        }

        return (decimal);
    }
};