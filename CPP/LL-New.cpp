#include <bits/stdc++.h>

using namespace std;

class Node{
    public:
    int data;
    Node* next;
    
    Node(int x){
        data=x;
        next=NULL;
    }
    
};

void insertAtHead(Node* &head, int data){
    Node* newNode = new Node(data);
    newNode->next=head;
    head=newNode;
}

void insertAtTail(Node* &head, int data){
    Node* newNode = new Node(data);
    Node* temp = head;
    
    if(head == NULL){
        head = newNode;
    }
    
    while(temp->next != NULL){
        temp = temp->next;
    }
    
    temp->next = newNode;
}

void insertBefore(Node* head, int pos, int data){
    Node* newNode = new Node(data);
    Node* temp = head;
    
    while(temp->next->data != pos){
        temp = temp->next;
    }
    
    newNode->next = temp->next;
    temp->next = newNode;
}

void insertAfter(Node* head, int pos, int data){
    Node* newNode = new Node(data);
    Node* temp = head;
    
    while(temp->data != pos){
        temp = temp->next;
    }
    
    newNode->next = temp->next;
    temp->next = newNode;
}

void deleteHead(Node* &head){
    if(head == NULL){
        return;
    }
    
    Node* temp = head;
    head = head->next;
    delete temp;
}

void deleteTail(Node* head){
    Node* temp = head;
    
    if(head == NULL){
        return;
    }
    
    while(temp->next->next != NULL){
        temp = temp->next;
    }
    
    delete temp->next;
    temp->next = NULL;
}

void display(Node* head){
    Node* temp=head;
    
    while(temp!=NULL){
        cout<<temp->data<<"->";
        temp=temp->next;
    }
       
    cout<<endl;
}

void reverse(Node* &head){
    Node* prev = NULL;
    Node* cur = head;
    Node* next; 
    
    while(cur != NULL){
        next = cur->next;
        cur->next = prev;
        
        prev = cur;
        cur = next;
    }
    
    // return prev;
    head = prev;
}

Node* reverseRecursive(Node* &head){
    if(head == NULL || head->next == NULL){
        return head;
    }
    
    Node* newHead = reverseRecursive(head->next);
    
    head->next->next = head;
    head->next = NULL;
    
    return newHead;
}

void findMid(Node* &head){
    Node* slow = head;
    Node* fast = head;
    
    while(fast != NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
    }
    
    cout<<"Mid of Linked List: "<<slow->data<<endl;
}

void createLoop(Node* head, int pos){
    Node* temp = head;
    Node* loopNode;
    
    while(temp->next != NULL){
        if(temp->data == pos){
            loopNode = temp;
        }
        temp = temp->next;
    }
    
    temp->next = loopNode;
    // delete loopNode;
}

int detectLoop(Node* &head){
    Node* slow = head;
    Node* fast = head;
    
    while(fast != NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;

        if(fast == slow){
            return 1;
        }
    }
    
    return 0;
}

void removeLoop(Node* &head){
    Node* slow = head;
    Node* fast = head;
    
    if(!detectLoop(head)){
        return;
    }
    
    while(fast != NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;

        if(fast == slow){
            break;
        }
    }
    
    slow = head;
    
    while(slow->next != fast->next){
        slow = slow->next;
        fast = fast->next;
    }
    
    fast->next = NULL;
}

    
int main(){
    
    Node* head=NULL;
    insertAtHead(head,1);
    insertAtTail(head,2);
    insertAtTail(head,3);
    // insertBefore(head, 3, 7);
    insertAtTail(head,4);
    // insertAfter(head, 4, 9);
    insertAtTail(head,5);
    
    cout<<detectLoop(head)<<endl;
    
    display(head);
    
    // deleteHead(head);
    // deleteTail(head);
    reverse(head);
    
    display(head);
    
    head = reverseRecursive(head);
    
    display(head);
    
    createLoop(head, 3);
    
    cout<<detectLoop(head)<<endl;
    
    removeLoop(head);

    display(head);
    
    findMid(head);
    
    return 0;
}