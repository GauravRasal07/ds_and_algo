//Binary Search Trees

#include <bits/stdc++.h>

using namespace std;

class node {
    public:
    int data;
    node* left;
    node* right;

    node(int val){
        data = val;
        left = NULL;
        right = NULL;
    }
};

void insert(node* &root, int val){
    node* newNode = new node(val);

    if(root == NULL){
        root = newNode;
        return root;
    }

    if(val < root->data){
        insert(root->left, val);
    } else if (val > root->data){
        insert(root->right, val);
    } else {
        cout << "The value is same as previous node: " << root->data << endl;
        return;
    }
}

void preorder(node* root){
    if(root == NULL){
        return;
    }
    
    cout << root->data << " -> ";
    preorder(root->left);
    preorder(root->right);
}

void postorder(node* root){
    if(root == NULL){
        return;
    }
    
    postorder(root->left);
    postorder(root->right);
    cout << root->data << " -> ";
}

void inorder(node* root){
    if(root == NULL){
        return;
    }
    
    inorder(root->left);
    cout << root->data << " -> ";
    inorder(root->right);
}

void deleteNode(node* root, int val){
    node* temp = root;
    node* parent = NULL;

    //Searching for the node
    while(temp->data != val && temp != NULL){
        parent = temp;

        if(temp->data < val){
            temp = temp->right;
        } else if( temp->data > val){
            temp = temp->left;
        }
    }

    
    if(temp == NULL){
        cout << "The node you're searching is not found" << endl;
        return;
    }


    //CASE 1: delete leaf node
    if(temp->left == NULL && temp->right == NULL){
        if(temp == root){
            root = NULL;
        } else if(parent->left == temp){
            parent->left = NULL;
        } else {
            parent->right = NULL;
        }

        delete temp;
    }

    //CASE 2: Node having only one child
    else if(temp->left == NULL && temp->right != NULL){
        if(parent->left == temp){
            parent->left = temp->right;
        } else {
            parent->right = temp->right;
        }

        delete temp;
    }

    else if(temp->left != NULL && temp->right == NULL){
        if(parent->left == temp){
            parent->left = temp->left;
        } else {
            parent->right = temp->left;
        }

        delete temp;
    }

    //CASE 3: Node having two childs
    else if(temp->left != NULL && temp->right != NULL){
        node* in_succ = temp->right;

        while(in_succ->left != NULL){
            in_succ = in_succ->left;
        }

        int data1 = in_succ->data;

        deleteNode(root, in_succ->data);

        temp->data = data1;
    }

}

int main(){
    node* root = new node(5);
    insert(root, 7);
    insert(root, 3);
    insert(root, 4);
    insert(root, 6);
    insert(root, 1);
    insert(root, 9);

    cout<<"\nThe Preorder traversal is: "<<endl;
    preorder(root);
    // cout<<"\nThe Inorder traversal is: "<<endl;
    // inorder(root);
    // cout<<"\nThe Postorder traversal is: "<<endl;
    // postorder(root);
    deleteNode(root, 7);
    cout<<"\nThe Preorder traversal is: "<<endl;
    preorder(root);

    return 0;
}