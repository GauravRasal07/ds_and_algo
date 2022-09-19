def delNode(head, k):
    # Code here
    i=2
    if(k==1):
        head=head.next
        return head
        
    def delete(head,k,i):
        prev=head
        temp=prev.next
        if temp==None or i>k:
            return head
            
        elif i==k:
            prev.next=temp.next
            return head
        else:
            
            delete(prev.next,k,i+1)
            return head
    ans=delete(head,k,i)
    return ans