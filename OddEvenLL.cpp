#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
struct ListNode{
    int val;
    ListNode* next;

    ListNode() : val(0), next(nullptr){}
    ListNode(int x) : val(x), next(nullptr){}
    ListNode(int x, ListNode* nex) : val(x), next(nex){}
    
};

ListNode* buildList(const vector<int> &input){
    if(input.size() == 0) return NULL;
    ListNode* head = new ListNode(input[0]);
    ListNode* curr = head;
    for(int i = 1; i < input.size(); i++){
        curr->next = new ListNode(input[i]);
        curr = curr->next;
    }
    return head;

}


class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {

        if(head == nullptr || head->next == nullptr){
            return head;
        }

        ListNode* even = head->next;
        ListNode* odd = head;
        ListNode* eHead = even;

        
        //attach all
      while (even != nullptr && even->next != nullptr) {
        odd->next = even->next;
        odd = odd->next;
        
        even->next = odd->next;
        even = even->next;
        }
        //attach last odd to eHead
        odd->next = eHead;
        return head;
    }
};

int main(){

    //input format: given the head of a linked list. 
    //head = [1,2,3,4,5]
    //output : [1,3,5,2,4]
    //input size of list, n

    int n;
    cin >> n;
    vector<int> input(n);

    for(int i = 0; i < n; i++){
        cin>> input[i];
    }
    ListNode* head = buildList(input);

    Solution s;

    ListNode* ans = s.oddEvenList(head);
    //function to print list 
    cout<< ans->val;
    while(ans->next){
        cout<<" ";

        cout<<ans->next->val;
        ans = ans->next;
    }
    cout << endl;

}