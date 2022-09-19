class node:
    def __init__(self, data):
        self.data = data
        self.next = None


def display(head):
    print("Your linked list is: ")

    itr = head

    while(itr != None):
        print(itr.data, end=" ")
        itr = itr.next
    print()


def add_to_head(head, data):
    new_node = node(data)

    if head is None:
        head = new_node
        return head
    
    new_node.next = head
    head = new_node
    return head


def add_to_end(head, data):
    new_node = node(data)

    if head is None:
        head = new_node
        return

    itr = head

    while itr.next != None:
        itr = itr.next

    itr.next = new_node


def reverse(head):
    prev, curr, nex = None, None, None

    if head is None or head.next is None:
        return head

    curr = head

    while curr != None:
        nex = curr.next
        curr.next = prev

        prev = curr
        curr = nex

    return prev


def reverseRecursive(head):
    if head is None or head.next is None:
        return head
    
    newHead = reverseRecursive(head.next)

    head.next.next = head
    head.next = None

    return newHead


def swap_nodes_in_pairs(head):
    if head is None or head.next is None:
        return head

    dummy = prev = node(0)
    dummy.next = head

    while head and head.next:
        temp = head.next

        head.next = temp.next
        temp.next = head
        prev.next = temp

        head = head.next
        prev = temp.next

    return dummy.next


head = node(2)
add_to_end(head, 3)
add_to_end(head, 4)
add_to_end(head, 5)
head = add_to_head(head, 1)
head = add_to_head(head, 0)
display(head)
head = swap_nodes_in_pairs(head)
display(head)
# head = reverse(head)
# display(head)
# head = reverseRecursive(head)
# display(head)