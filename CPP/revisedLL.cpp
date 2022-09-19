#include <iostream>
#include <stdio.h>
using namespace std;

class Node {
    public:
        int data;
        Node* next;
    
    Node(int val){
        data = val;
        next = NULL;
    };
};
    
    
void insertAtHead(Node* &head, int val){
    Node* newNode = new Node(val);
    
    if(head == NULL){
        head = newNode;
        cout<<"Node inserted at head in empty list"<<endl;
        return;
    }
    
    Node* temp = head;
    
    head = newNode;
    
    head->next = temp;
    
    cout<<"Created a new Head with given value"<<endl;
    
}


void insertAtTail(Node* &head, int val){
    Node* newNode = new Node(val);
    
    if(head == NULL){
        head = newNode;
        cout<<"Inserted node at head as list was empty"<<endl;
        return;
    }
    
    Node* temp = head;
    
    while(temp->next != NULL){
        temp = temp->next;
    }
    
    temp->next = newNode;
    cout<<"Node Inserted at Tail"<<endl;
}


void insertAtPosition(Node* &head, int val, int key){
    Node* newNode = new Node(val);
    
    if(head == NULL){
        head = newNode;
        cout<<"Inserted node at head as list was empty"<<endl;
        return;
    }
    
    Node* temp = head;
    while(temp != NULL){
        if(temp->data == key){
            Node* temp1 = temp->next;
            temp->next = newNode;
            newNode->next = temp1;
            cout<<"Inserted Node after the mentioned element"<<endl;
            return;
        }
        
        temp = temp->next;
    }
    
}

void displayList(Node* head){
    Node* temp = head;
    
    if(head == NULL){
        cout<<"The list is empty"<<endl;
        return;
    }

    while(temp != NULL){
        cout<<temp->data<<" ";
        
        temp = temp->next;
    }
    
    cout<<endl;
}

void deleteNode(Node* &head, int val){
    if(head == NULL){
        cout<<"The List is empty"<<endl;
        return;
    }
    
    else if(head->data == val){
        Node* t = head->next;
        
        delete head;
        
        head = t;
        // return;
    }
    
    Node* temp = head;
    while(temp->next != NULL){
        cout << temp->data<< " -> ";
        if(temp->next->data == val){
            Node* toDelete = temp->next;
            
            temp->next = temp->next->next;
            
            delete toDelete;
            // break;
        }
        
        temp = temp->next;
    }
}

void reverseList(Node* &head){
    Node* prev = NULL;
    Node* current = head;
    Node* next;
    
    while(current != NULL){
        next = current->next;
        current->next = prev;
        
        prev = current;
        current = next;
    }
    
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

void makeCycle(Node* head, int pos){
    Node* temp = head;
    Node* start;
    int cnt = 0;
    
    while(temp->next != NULL){
        if(cnt == pos){
            start = temp;
        }
        
        temp = temp->next;
        cnt ++;
    }
    
    temp->next = start;
}

bool detectCycle(Node* head){
    Node* hare = head;
    Node* tortoise = head;
    
    while(hare != NULL && hare->next != NULL){
        hare = hare->next->next;
        tortoise = tortoise->next;
        
        if(hare == tortoise){
            return true;
        }
    }
    
    return false;
}

void removeCycle(Node* head){
    Node* hare = head;
    Node* tortoise = head;
    
    do{
        hare = hare->next->next;
        tortoise = tortoise->next;
    } while (hare != tortoise);
    
    hare = head;
    
    while(hare->next == tortoise->next){
        hare = hare->next;
        tortoise = tortoise->next;
    }
    
    tortoise->next = NULL;
}



int main()
{
    // Node* Head = NULL;
    
    // insertAtHead(Head, 3);
    // insertAtHead(Head, 2);
    // insertAtHead(Head, 1);
    
    // insertAtTail(Head, 5);
    // insertAtTail(Head, 6);
    
    // insertAtPosition(Head, 4, 3);
    
    // displayList(Head);
    
    Node* Head = NULL;
    // displayList(Head);
    insertAtTail(Head, 7);
    insertAtTail(Head, 7);
    insertAtTail(Head, 7);
    insertAtTail(Head, 7);
    // insertAtTail(Head, 7);
    
    // insertAtHead(Head, 0);
    
    // insertAtPosition(Head, 3, 2);
    
    cout<<"Original Linked List is : ";
    displayList(Head);

    deleteNode(Head, 7);
    cout<<"Linked List after deletion is : ";
    displayList(Head);

    // makeCycle(Head, 4);
    // cout<<detectCycle(Head)<<endl;
    // removeCycle(Head);
    
    // cout<<"Removed cycle Linked List is : ";
    // displayList(Head);
    
    
    // deleteNode(Head, 1);
    // deleteNode(Head, 4);
    // cout<<"Linked List after deletion is : ";
    // displayList(Head);
    
    // reverseList(Head);
    // Head = reverseRecursive(Head);
    // cout<<"Reversed Linked List is : ";
    // displayList(Head);
    

    return 0;
}