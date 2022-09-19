# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def get_length(self, head):
        length = 0
        temp = head
        
        while temp:
            temp = temp.next
            length += 1
            
        return length
    
    
    def getIntersectionNode(self, headA, headB):
        length_A = self.get_length(headA)
        length_B = self.get_length(headB)
        
        diff = 0
        temp_A = headA
        temp_B = headB
        
        if length_A < length_B:
            diff = length_B - length_A
            
            while diff != 0:
                temp_B = temp_B.next
                diff -= 1
            
        else:
            diff = length_A - length_B
            
            while diff != 0:
                temp_A = temp_A.next
                diff -= 1
                
        while temp_A and temp_B:
            if temp_A == temp_B:
                return temp_A
            
            temp_A = temp_A.next
            temp_B = temp_B.next
            
        return None
        