#include <stdio.h>
#include <iostream>
using namespace std;

class node {
    public :
        int data;
        node* next;
        
    node(int val){
        data = val;
        next = NULL;
    };
};

void insert(node* &Head, int val, int key){
    node* n = new node(val);
    
    node* temp = Head;
    while(temp != NULL){
        if(temp->data == key){
            
            node* temp_1 = temp->next;
            temp->next = n;
            n->next = temp_1;
        }
        
        temp = temp->next;
    }
}

void insertAtTail(node* &Head, int val){
    node* n = new node(val);
    
    if(Head == NULL){
        Head = n;
        return;
    }
    
    node* temp = Head;
    while(temp->next != NULL){
        temp = temp->next;
    }
    
    temp->next = n;
};

void insertAtHead(node* &Head, int val){
    node* n = new node(val);
    
    n->next = Head;
    Head = n;
}

bool search(node* Head, int key){
    node* temp = Head;
    
    while(temp != NULL){
        if(temp->data == key){
            return true;
        }
        
        temp = temp->next;
    }
    
    return false;
}

void Display(node* Head){
    node* temp = Head;
    
    while(temp != NULL){
        cout<<temp->data<<" ";
        
        temp = temp->next;
    }
    cout<<endl;
};

void Delete(node* &Head, int key){
    if(Head == NULL){
        // cout<<'The list is empty'<<endl;
        return;
    }
    
    else if(Head->data == key){
        node* temp = Head->next;
        
        delete Head;
        Head = temp;
        return;
    }
    
    node* temp = Head;
    
    while(temp->next->data != key){
        temp = temp->next;
    }
    
    node* toDelete = temp->next;
    temp->next = temp->next->next;
    
    delete toDelete;
}

void reverse(node* &Head){
    node* prevptr = NULL;
    node* current = Head;
    node* nextptr;
    
    while(current != NULL){
        nextptr = current->next;
        current->next = prevptr;
        
        prevptr = current;
        current = nextptr;
    }
    
    Head = prevptr;
}

node* reverseRecursive(node* &Head){
    if(Head == NULL || Head->next == NULL){
        return Head;
    }
    
    node* newHead = reverseRecursive(Head->next);
    Head->next->next = Head;
    Head->next = NULL;
    
    return newHead;
}

node* merge(node* &p1, node* &p2){
    node* h1 = p1;
    node* h2 = p2;
    node* newHead = new node(-1);
    node* h3 = newHead;
    
    while(h1 != NULL && h2 != NULL){
        if(h1->data <= h2->data){
            h3->next = h1;
            h1 = h1->next;
        } else {
            h3->next = h2;
            h2 = h2->next;
        }
        
        h3 = h3->next;
    }
    
    while(h1 != NULL){
        h3->next = h1;
        h1 = h1->next;
        h3 = h3->next;
    }

    while(h2 != NULL){
        h3->next = h2;
        h2 = h2->next;
        h3 = h3->next;
    }

    return newHead->next;
}

int main(){
    cout<<"Heyy There, We're Learning Linked List\n"<<endl;
    
    node* Head = NULL;
    node* secondHead = NULL;
    insertAtHead(Head, 0);
    insertAtTail(Head, 1);
    insertAtTail(Head, 3);
    insertAtTail(Head, 5);
    
    // insert(Head, 3, 2);

    insertAtTail(secondHead, 2);
    insertAtTail(secondHead, 4);
    insertAtTail(secondHead, 6);
    insertAtTail(secondHead, 7);

    // insertAtHead(secondHead, );

    
    cout<<"Original Linked List is : \n";
    Display(Head);
    Display(secondHead);
    cout << endl;

    cout<<"Merged Linked List is : \n";
    Display(merge(Head, secondHead));

    // node* newHead = reverseRecursive(Head);
    // cout<<"\nReversed Linked List is : ";
    // Display(newHead);
    
    // reverse(newHead);
    // cout<<"\nAgain Reversed Linked List is : ";
    // Display(newHead);
    
    return 0;
}